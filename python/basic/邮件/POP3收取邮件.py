# coding=utf-8
import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

email = '635943647@qq.com'  # 邮箱名
password = 'mdtrergmfslkbdgi'  # QQ邮箱授权码
pop3_server = 'imap.qq.com'  # 收取邮件的服务器
server = poplib.POP3(pop3_server)  # 连接到POP3服务器
server.set_debuglevel(1)  # 可以打开或关闭调试信息
print(server.getwelcome())  # 打印POP3服务器的欢迎文字:
server.user(email)  # 身份认证--用户名
server.pass_(password)  # 身份认证--密码
print(server.stat())  # stat()返回邮件数量和占用空间
resp, mails, octets = server.list()  # list()返回所有邮件的编号:
print(mails)
resp
mails
octets
# server.dele(index)  # 可以根据邮件索引号直接从服务器删除邮件
# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index-4)  # lines存储了邮件的原始文本的每一行

msg_content = '\r\n'.join(lines)  # 可以获得整个邮件的原始文本:
msg = Parser().parsestr(msg_content)  # 将邮件内容解析为Message对象
# 但是这个Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层
msg.get('From', '')

server.quit()  # 关闭连接:
