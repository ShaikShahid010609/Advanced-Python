###processpool code
from concurrent.futures import ProcessPoolExecutor
import os
import time

def square(num):
    print(f"Processing {num} in PID: {os.getpid()}")
    time.sleep(2)
    return num * num

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, [1, 2, 3, 4, 5])

    print("Results:")
    for result in results:
        print(result)
