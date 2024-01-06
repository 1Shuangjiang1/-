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


# 使用示例
host_server = 'smtp.qq.com'
sender_qq = 'yangqifanbq@qq.com'
pwd = 'ligsaipzxolvhcec'
receiver = 'yangqifanbq@gmail.com'
mail_title = 'Python自动发送html格式的邮件'
mail_content = "您好，<p>这是使用python登录QQ邮箱发送HTNL格式邮件的测试：</p> <p><a href='https://blog.csdn.net/weixin_44827418?spm=1000.2115.3001.5113'>CSDN个人主页</a></p>"

# 创建邮件发送器实例
emailer = EmailSender(host_server, sender_qq, pwd, receiver, mail_title)
# 调用方法发送邮件
emailer.send_email(mail_content)

# def main():
#     # 定义邮件服务器和账户信息
#     host_server = 'smtp.qq.com'
#     sender_qq = 'yangqifanbq@qq.com'
#     pwd = 'ligsaipzxolvhcec'  # 请确保这是你的授权码，而非密码
#     receiver = 'yangqifanbq@gmail.com'
#     mail_title = 'Python自动发送html格式的邮件'
#
#     # 邮件正文内容
#     mail_content = "您好，<p>这是使用python登录QQ邮箱发送HTML格式邮件的测试：</p><p><a href='https://blog.csdn.net/weixin_44827418?spm=1000.2115.3001.5113'>CSDN个人主页</a></p>"
#
#     # 创建EmailSender对象
#     emailer = EmailSender(host_server, sender_qq, pwd, receiver, mail_title)
#
#     # 发送邮件
#     emailer.send_email(mail_content)
#
# if __name__ == "__main__":
#     main()


# host_server = 'smtp.qq.com'  #qq邮箱smtp服务器
# sender_qq = 'yangqifanbq@qq.com' #发件人邮箱
# pwd = 'ligsaipzxolvhcec'
# receiver = 'yangqifanbq@gmail.com'
# mail_title = 'Python自动发送html格式的邮件' #邮件标题
#
# #邮件正文内容
# mail_content = "您好，<p>这是使用python登录QQ邮箱发送HTNL格式邮件的测试：</p> <p><a href='https://blog.csdn.net/weixin_44827418?spm=1000.2115.3001.5113'>CSDN个人主页</a></p>"
#
# msg = MIMEMultipart()
# msg["Subject"] = Header(mail_title,'utf-8')
# msg["From"] = sender_qq
# msg["To"] = Header("测试邮箱","utf-8")
#
# # msg.attach(MIMEText(mail_content,'html'))
# # attachment = MIMEApplication(open('./test.xlsx','rb').read())
# # attachment["Content-Type"] = 'application/octet-stream'
# # # 给附件重命名
# # basename = "test.xlsx"
# # attachment.add_header('Content-Dispositon','attachment',filename=('utf-8', '', basename))#注意：此处basename要转换为gbk编码，否则中文会有乱码。
# # msg.attach(attachment)
#
#
# try:
#     smtp = SMTP_SSL(host_server) # ssl登录连接到邮件服务器
#     smtp.set_debuglevel(1) # 0是关闭，1是开启debug
#     smtp.ehlo(host_server) # 跟服务器打招呼，告诉它我们准备连接，最好加上这行代码
#     smtp.login(sender_qq,pwd)
#     smtp.sendmail(sender_qq,receiver,msg.as_string())
#     smtp.quit()
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("无法发送邮件")

