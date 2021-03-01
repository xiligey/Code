#coding=utf-8
__name__='xiligey'
#1.使用os.system函数运行其他程序或脚本
import os
# os.system('notepad python.txt')
# print 1

# 2.使用ShellExecute函数运行其他程序
from win32api import ShellExecute
# ShellExecute(hwnd,op,file,params,dir,bShow)
# hwnd:父窗口的句柄，若没有则为0
# op：要进行的操作，为open，print or 空
# file：要运行的程序或脚本
# params 要向程序传递的参数，如果打开的是文件则为空
# dir：程序初始化的目录
# bShow：是否显示窗口
# ShellExecute(0,'open','notepad.exe','python.txt','',1)
# ShellExecute(0,'open','http://www.baidu.com','','',1)
# ShellExecute(0,'open','F:\\Love\\Lady Antebellum - Need You Now.ape','','',1)
# ShellExecute(0,'open','D:\Python\Code\Crawler\HanhanBlog.py','','',1)


import os
import time
# print time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
#
# while 1:
#     time.sleep(30)
#     if time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))=='2016-03-08-13-30':
#         ShellExecute(0,'open','F:\\Love\\Lady Antebellum - Need You Now.ape','','',1)
#         break
#
# print '上班'

#3.使用CreateProcess函数
import win32process
from win32process import CreateProcess
CreateProcess('c:\\windows\\notepad.exe', '', None, None, 0, win32process.CREATE_NO_WINDOW, None, None,
              win32process.STARTUPINFO())
