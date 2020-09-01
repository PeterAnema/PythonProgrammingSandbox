# countthread.py

import time
from threading import Thread

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    threads = list()
    for _ in range(3):
        t = Thread(target=count)
        threads.append(t)
        t.start()

    for index, t in enumerate(threads):
        t.join()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")