from concurrent.futures import ThreadPoolExecutor
import threading
import time

def task(num):
    print(f"Task {num} running in {threading.current_thread().name}")
    time.sleep(2)
    return num * num

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, [1, 2, 3, 4, 5])

print("Results:")
for result in results:
    print(result)