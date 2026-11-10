import timeit
 
def otp_while(entries, correct="4821"):
    """while design: counter moves only on a real (non-blank) attempt."""
    attempts, i = 0, 0
    while attempts < 3:
        if i >= len(entries): break
        code = entries[i].strip(); i += 1
        if code == "":
            continue                      # blank: not an attempt
        attempts += 1                     # counter updated AFTER the blank check
        if code == correct:
            return f"verified on attempt {attempts}"
    else:
        return "LOCKED for 30 minutes"    # loop-else: runs only if no break
    return "ended (no more input)"
 
def otp_for(entries, correct="4821"):
    it = iter(entries)
    for attempt in range(3):
        while True:                       # skip blanks without using an attempt
            code = next(it, None)
            if code is None: return "ended (no more input)"
            if code.strip() != "": break
        if code.strip() == correct:
            return f"verified on attempt {attempt + 1}"
        else:
            pass                          # placeholder: e.g. log the failure later
    else:
        return "LOCKED for 30 minutes"
 
def otp_extended(entries, security_ok, correct="4821"):
    """Changed condition: 3 attempts, +2 if the security question is right."""
    limit, attempts, i = 3, 0, 0
    while attempts < limit:
        if i >= len(entries): return "ended (no more input)"
        code = entries[i].strip(); i += 1
        if code == "": continue
        attempts += 1
        if code == correct: return f"verified on attempt {attempts}"
        if attempts == 3 and limit == 3 and security_ok:
            limit = 5                     # extra attempts granted once
    return "LOCKED for 30 minutes"
 
def otp_recursive(entries, i=0, attempts=0, correct="4821"):
    if attempts == 3: return "LOCKED for 30 minutes"
    if i >= len(entries): return "ended (no more input)"
    code = entries[i].strip()
    if code == "": return otp_recursive(entries, i + 1, attempts, correct)
    if code == correct: return f"verified on attempt {attempts + 1}"
    return otp_recursive(entries, i + 1, attempts + 1, correct)
 
cases = {"right on 2nd": ["1111", "4821"], "blank then right": ["", "4821"],
         "3 wrong": ["1", "2", "3"], "blanks + 3 wrong": ["", "1", "", "2", "3"]}
for name, e in cases.items():
    print(f"{name:<18} while: {otp_while(e):<24} for: {otp_for(e):<24} recursive: {otp_recursive(e)}")
print("extended, security OK  :", otp_extended(["1","2","3","4","4821"], True))
print("extended, security FAIL:", otp_extended(["1","2","3","4","4821"], False))
 
# Bug demo: counter updated before blank check
def wrong_counter(entries, correct="4821"):
    attempts = 0
    for code in entries:
        attempts += 1                     # BUG: blank counted
        if code.strip() == "": continue
        if code == correct: return f"verified on attempt {attempts}"
        if attempts == 3: return "LOCKED"
    return "no result"
print("wrong counter, ['', '1', '2', '4821'] ->", wrong_counter(["", "1", "2", "4821"]), "(blank wasted an attempt; correct OTP never reached)")
print("right counter, ['', '1', '2', '4821'] ->", otp_while(["", "1", "2", "4821"]))
n = 1000
print("time for a=3 attempts x 100000 runs:",
      f"while {timeit.timeit(lambda: otp_while(['1','2','3']), number=100000):.3f}s,",
      f"recursive {timeit.timeit(lambda: otp_recursive(['1','2','3']), number=100000):.3f}s")

