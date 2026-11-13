import logging
import time

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s: %(message)s")

pm25_values = [48, 95, 121]
start = time.perf_counter()

for value in pm25_values:
    assert value >= 0, "Negative PM2.5 reading"
    logging.info("Validated PM2.5 value: %s", value)

elapsed = time.perf_counter() - start
print("Execution time:", round(elapsed, 6), "seconds")
