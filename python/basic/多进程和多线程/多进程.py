# coding=utf-8
from multiprocessing import Process
import os

# 启动一个子进程并等待其结束


def run_proc(name):
    print 'run chile process %s %s' % (name, os.getpid())
    print 'Parent process %s' % os.getpid()


# if __name__ == '__main__':
#     p = Process(target=run_proc, args=('test', ))
#     print 'Process will start'
#     p.start()
#     p.join()  # join方法可以等待子进程结束后再继续往下运行, 通常用于进程间的同步
#     print 'Process end'
#

# 如果启动大量子进程, 可以用进城池的方法批量创建子进程
from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print 'Run task %s %s' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'The %s runs %0.2f seconds' % (name, end - start)


# if __name__ == '__main__':
#     print 'Parent process %s' % os.getpid()
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i, ))
#     print 'waiting for all subprocesses done...'
#     p.close()
#     p.join()
#     print 'All subprocesses done'

# 进程间通信
from multiprocessing import Process, Queue
import os, time, random


def write(q):
    for value in ['A', 'B', 'C', 'D']:
        print 'put %s to queue' % value
        q.put(value)
        time.sleep(1)


def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue' % value


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))

    pw.start()
    pr.start()
    pw.join()
    # pr.join()
    pr.terminate()
