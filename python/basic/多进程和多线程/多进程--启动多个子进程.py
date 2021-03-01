from multiprocessing import Pool
import os
import time
import random


# 如果要启动多个子进程,需要进程池

def long_time_task(name):
    print('运行任务%s(%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("任务%s运行时长%0.2f秒" % (name, end - start))


if __name__ == '__main__':
    print("父进程%s" % os.getpid())
    p = Pool(4)
    for i in range(100):
        p.apply_async(long_time_task, args=(i,))
    print("等待所有子进程运行完毕")
    p.close()
    p.join()
    print("所有子进程运行完毕")
