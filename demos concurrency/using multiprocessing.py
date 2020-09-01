from multiprocessing import Process
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    processes = list()
    for _ in range(3):
        p = Process(target=count)
        processes.append(p)
        p.start()

    for index, p in enumerate(processes):
        p.join()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")