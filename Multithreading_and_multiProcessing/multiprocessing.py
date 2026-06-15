from multiprocessing import Process
import time

def print_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(0.5)

def print_alphabets():
    for ch in "ABCDEFGHIJ":
        print(ch)
        time.sleep(0.5)

if __name__ == "__main__":
    p1 = Process(target=print_numbers)
    p2 = Process(target=print_alphabets)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")