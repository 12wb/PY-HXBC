import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

send='2654158887@qq.com'
password='euguhnqyfficeaei'
recv=['2654158887@qq.com']

#邮件类型为"multipart/alternative"的邮件包括纯文本正文（text/plain）和超文本正文（text/html）。
#邮件类型为"multipart/related"的邮件正文中包括图片，声音等内嵌资源。
#邮件类型为"multipart/mixed"的邮件包含附件。向上兼容，如果一个邮件有纯文本正文，超文本正文，内嵌资源，附件，则选择mixed类型。
msgRoot = MIMEMultipart('mixed')
msgRoot['From']=Header('你的朋友','utf-8')
msgRoot['To']=Header('测试人员','utf-8')
msgRoot['Subject']=Header('邮件构建测试','utf-8')

#文本
text_text='这个就是测试文本！'
msg_text=MIMEText(text_text,'plain','utf-8')
#超文本
mail_msg = """
<p>Python 邮件发送网页...</p>
<p><a href="http://www.baidu.com">搜索链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msg_html=MIMEText(mail_msg, 'html', 'utf-8')


# 指定图片为当前目录
with open('test.jpg','rb') as file:
    msg_Image = MIMEImage(file.read())
    msg_Image.add_header('Content-ID', '<image1>')

#加载附件
with open('1111.txt','rb') as sendfile:
    msg_att=MIMEText(sendfile.read(),'base64','utf-8')
    msg_att["Content-Type"] = 'application/octet-stream'
    msg_att.add_header('Content-Disposition', 'attachment', filename='aaa.txt')

msgRoot.attach(msg_text)
msgRoot.attach(msg_html)
msgRoot.attach(msg_Image)
msgRoot.attach(msg_att)


try:
    smtp=smtplib.SMTP('smtp.qq.com')
    smtp.login(send,password)
    smtp.sendmail(send,recv,msgRoot.as_string())
    smtp.quit()
except:
    print('cuowu')