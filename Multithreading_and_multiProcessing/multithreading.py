import threading
import time

def print_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(0.5)

def print_alphabets():
    for ch in "ABCDEFGHIJ":
        print(ch)
        time.sleep(0.5)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_alphabets)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Done!")
