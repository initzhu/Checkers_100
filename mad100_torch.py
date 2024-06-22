# import threading
# import time

# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print(f"{threadName}: {time.ctime(time.time())}")

# # 创建两个线程
# try:
#     thread1 = threading.Thread(target=print_time, args=("Thread-1", 2))
#     thread2 = threading.Thread(target=print_time, args=("Thread-2", 4))
#     thread1.start()
#     thread2.start()
# except:
#     print("Error: unable to start thread")


# import torch
# import torch.multiprocessing as mp

# def worker(rank):
#     print(f"Worker {rank} is doing some work.")

# if __name__ == "__main__":
#     num_processes = 4
#     processes = []

#     for rank in range(num_processes):
#         process = mp.Process(target=worker, args=(rank,))
#         processes.append(process)
#         process.start()

#     for process in processes:
#         process.join()
