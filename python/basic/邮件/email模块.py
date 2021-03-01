"""
email模块下有mime包，mime英文全称为“Multipurpose Internet Mail Extensions”，
即多用途互联网邮件扩展，是目前互联网电子邮件普遍遵循的邮件技术规范。

该mime包下常用的有三个模块：text，image，multpart。
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

"""
继承关系：
- Message 整个邮件
    - MiMeMultipart 多个单独部分组成的多部分组件
    - MiMeNonMultipart  单个组件
        - MIMEMessage   单个信息
        - MIMEText      单个文本
        - MIMEImage     单个图片
"""
# 添加普通文本
text = MIMEText('你好!\n\t我是犀利哥，请多指教！', 'plain', _charset='utf-8')

# 添加超文本
html = MIMEText("""
<html>  
  <body>  
    <p> 
       Here is the <a href="http://www.baidu.com">link</a> you wanted.
    </p> 
  </body>  
</html>  
""", 'html', 'utf-8')

# 添加附件
file = open('邮件/email模块.py', 'rb').read()
attachment = MIMEText(file, 'base64', 'utf-8')
attachment['Content-Type'] = 'application/octet-stream'
attachment['Content-Disposition'] = 'attachment; filename="显示的名字.txt"'

# 添加图片
image = open('邮件/1.png', 'rb').read()
image = MIMEImage(image)
image.add_header('Content-ID', '<image1>')

"""
multipart说明

常见的multipart类型有三种：multipart/alternative, multipart/related和multipart/mixed。

邮件类型为"multipart/alternative"的邮件包括纯文本正文（text/plain）和超文本正文（text/html）。

邮件类型为"multipart/related"的邮件正文中包括图片，声音等内嵌资源。

邮件类型为"multipart/mixed"的邮件包含附件。向上兼容，如果一个邮件有纯文本正文，超文本正文，内嵌资源，附件，则选择mixed类型。
"""
msg = MIMEMultipart('mixed')
msg['Subject'] = '主题'
msg['From'] = ''  # 发件人
msg['To'] = ''  # 收件人，可以是列表
msg['Date'] = ''  # 时间，不设置也可以

"""
msg.add_header(_name,_value,**_params):添加邮件头字段。

msg.as_string():是将msg(MIMEText对象或者MIMEMultipart对象)变为str,如果只有一个html超文本正文或者plain普通文本正文的话，一般msg的类型可以是MIMEText；如果是多个的话，就都添加到MIMEMultipart，msg类型就变为MIMEMultipart。

msg.attach(MIMEText对象或MIMEImage对象):将MIMEText对象或MIMEImage对象添加到MIMEMultipart对象中。MIMEMultipart对象代表邮件本身，MIMEText对象或MIMEImage对象代表邮件正文。

以上的构造的文本，超文本，附件，图片都何以添加到MIMEMultipart('mixed')中：
"""
msg.attach(text)
msg.attach(image)
msg.attach(attachment)
msg.attach(html)
