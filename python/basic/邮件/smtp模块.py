import smtplib

# 邮件发送流程
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')  # smtp地址和端口
smtp.login('user', 'password')  # 登陆，需要用户名和密码
smtp.sendmail('from_addr', 'to_addr', msg='')  # 发送邮件：发件人、收件人、邮件内容
smtp.quit()  # 退出

"""
常用邮箱的smtp地址：
    新浪邮箱：smtp.sina.com
    新浪VIP：smtp.vip.sina.com
    搜狐邮箱：smtp.sohu.com
    126邮箱：smtp.126.com
    139邮箱：smtp.139.com
    163网易邮箱：smtp.163.com

邮箱的端口：一般为25

邮件内容：一般是msg.as_string():as_string()是将msg(MIMEText对象或者MIMEMultipart对象)变为str。
"""
