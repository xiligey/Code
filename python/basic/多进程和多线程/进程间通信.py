from multiprocessing import Process, Queue
import os
import time
import random


# 进程之间需要相互通信的,Queue Pipes方式都可以实现通信
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
def write(q):
    print("写入的进程%s" % os.getpid())
    for value in ['A', 'B', 'C']:
        print("把%s放入队列" % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print("读取的进程%s" % os.getpid())
    while True:
        value = q.get(True)
        print('从队列中获取%s' % value)


if __name__ == '__main__':
    # 父进程创建queue,并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()  # 启动子进程pw,写入
    pr.start()  # 启动子进程pr,读取
    pw.join()
    pr.terminate()  # pr进程里是死循环,只能强行终止
