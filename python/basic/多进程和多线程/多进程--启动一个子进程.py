from multiprocessing import Process
import os


def run_process(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print("Parent process %s." % os.getpid())
    p = Process(target=run_process, args=('test',))  # 创建子进程时需要传入一个执行函数和函数的参数数组
    print("Child process will start.")
    p.start()  # 启动子进程
    p.join()  # join方法可以等待子进程结束后再继续往下运行,通常用于进程间的同步
    print('Child process end.')
