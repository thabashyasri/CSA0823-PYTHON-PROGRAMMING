import re, timeit
 
def normalise(text):
    """'tn 09 ab 1234' -> 'TN09AB1234'"""
    return text.strip().replace(" ", "").replace("-", "").upper()   # TODO 1
 
def is_valid(reg):
    """2 letters, 2 digits, 1 or 2 letters, 4 digits."""
    if len(reg) not in (9, 10):                                      # TODO 2
        return False
    series = reg[4:-4]
    return (reg[:2].isalpha() and reg[2:4].isdigit()
            and series.isalpha() and len(series) in (1, 2)
            and reg[-4:].isdigit())
 
def format_plate(reg):
    """'TN09AB1234' -> 'TN 09 AB 1234' (valid input only)."""
    if not is_valid(reg):
        raise ValueError("invalid registration number")
    return " ".join([reg[:2], reg[2:4], reg[4:-4], reg[-4:]])
 
for raw in ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234", "TN 22 1234 AB"]:
    reg = normalise(raw)
    print(f"{raw:15} -> {reg:11} {'valid' if is_valid(reg) else 'INVALID'}")
 
print("\nMy six predicted inputs:")
mine = ["tn 09 ab 1234", "TN-09-AB-1234", "Tn09Ab1234", "  ka01m0007 ", "TN09AB123", "T109AB1234"]
for raw in mine:
    reg = normalise(raw)
    print(f"{raw!r:18} -> {reg:11} {'valid  -> ' + format_plate(reg) if is_valid(reg) else 'INVALID'}")
 
print("\nSlicing demo:")
for s in ("KA01M0007", "TN09AB1234"):
    print(f"{s} len={len(s)}  s[-4:]={s[-4:]!r}  s[4:-4]={s[4:-4]!r}")
t = "tn09"; u = t.upper(); print("text.upper() leaves text unchanged:", t, "->", u)
try:
    t[0] = "T"
except TypeError as e:
    print("TypeError:", e)
 
PAT = re.compile(r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}")
def is_valid_re(reg): return PAT.fullmatch(reg) is not None
samples = ["TN09AB1234", "KA01M0007", "TN9AB1234", "TN221234AB", "TN09ABC1234", "TN09AB12345"]
print("slicing == regex on samples:", all(is_valid(s) == is_valid_re(s) for s in samples))
print("time 200,000 checks: slicing %.3f s, regex %.3f s" % (
    timeit.timeit(lambda: is_valid("TN09AB1234"), number=200000),
    timeit.timeit(lambda: is_valid_re("TN09AB1234"), number=200000)))

