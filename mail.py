import smtplib
import string
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication # 用于添加附件

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smtplib import SMTP_SSL


class EmailSender:
    def __init__(self, host_server, sender_qq, pwd, receiver, mail_title):
        self.host_server = host_server
        self.sender_qq = sender_qq
        self.pwd = pwd
        self.receiver = receiver
        self.mail_title = mail_title

    def send_email(self, mail_content):
        msg = MIMEMultipart()
        msg["Subject"] = Header(self.mail_title, 'utf-8')
        msg["From"] = self.sender_qq
        msg["To"] = Header("测试邮箱", "utf-8")

        # 假设这是HTML邮件内容
        msg.attach(MIMEText(mail_content, 'html'))

        # 如果需要发送附件，可以取消以下注释并确保路径正确
        # attachment = MIMEApplication(open('./test.xlsx', 'rb').read())
        # attachment["Content-Type"] = 'application/octet-stream'
        # basename = "test.xlsx"
        # attachment.add_header('Content-Dispositon', 'attachment', filename=('utf-8', '', basename))
        # msg.attach(attachment)

        try:
            smtp = SMTP_SSL(self.host_server)  # ssl登录连接到邮件服务器
            smtp.set_debuglevel(1)  # 0是关闭，1是开启debug
            smtp.ehlo(self.host_server)  # 跟服务器打招呼
            smtp.login(self.sender_qq, self.pwd)
            smtp.sendmail(self.sender_qq, self.receiver, msg.as_string())
            smtp.quit()
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("无法发送邮件")

def send_verification_email(host_server, sender_qq, pwd, receiver, mail_title, mail_content):
    email_sender = EmailSender(host_server, sender_qq, pwd, receiver, mail_title)
    email_sender.send_email(mail_content)


# 使用示例
# host_server = 'smtp.qq.com'
# sender_qq = 'yangqifanbq@qq.com'
# pwd = 'ligsaipzxolvhcec'
# receiver = 'yangqifanbq@gmail.com'
# mail_title = 'Python自动发送html格式的邮件'
# mail_content = "您好，<p>这是使用python登录QQ邮箱发送HTNL格式邮件的测试：</p> <p><a href='https://blog.csdn.net/weixin_44827418?spm=1000.2115.3001.5113'>CSDN个人主页</a></p>"
#
# # 创建邮件发送器实例
# emailer = EmailSender(host_server, sender_qq, pwd, receiver, mail_title)
# # 调用方法发送邮件
# emailer.send_email(mail_content)

