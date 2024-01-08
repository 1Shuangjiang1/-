from tkinter import messagebox
import random
from function.mail import *
import tkinter as tk
from tkinter import ttk
import string

#启帆的邮箱验证码和注册功能

def generate_random_code(self, length=6):
    """生成一个指定长度的随机验证码，包含数字和字母。"""
    characters = string.ascii_letters + string.digits  # 包括字母和数字
    return ''.join(random.choice(characters) for i in range(length))


def send_verification_code(self, email):
    # 在这里实现发送验证码到邮箱的逻辑
    # 为简化示例，这里返回一个假的验证码 "123456"
    # print(f"发送验证码到 {email}")
    # return "123456"
    host_server = 'smtp.qq.com'
    sender_qq = 'yangqifanbq@qq.com'
    pwd = 'ligsaipzxolvhcec'  # 注意这通常是邮箱的授权码，并非登录密码
    print(email)
    receiver = email  # 直接使用方法参数
    mail_title = '邮箱注册验证码'
    # verification_code = '123456'  # 正常情况下这里应该是随机生成的验证码
    verification_code = self.generate_random_code(6)
    mail_content = f'<p>这是使用python登录QQ邮箱发送HTNL格式邮件的测试：您的邮箱验证码为：{verification_code}</p>'

    try:
        # 调用封装好的邮件发送函数
        address_book.mail.send_verification_email(host_server, sender_qq, pwd, receiver, mail_title, mail_content)
        return verification_code
    except Exception as e:
        print("邮件发送失败:", e)
        return None


def validate_code(self, input_code, correct_code):
    # 校验输入的验证码是否与正确的验证码匹配
    return input_code == correct_code


def register_user(self, username, password, email):
    if self.check_user_exists(username):
        messagebox.showerror("注册失败", "该用户名已存在！")
        return False
    else:
        # 获取用户输入的验证码
        correct_code = self.send_verification_code(email)
        verification_window = tk.Toplevel(self.root)
        verification_window.title("请输入验证码")

        verification_label = ttk.Label(verification_window, text="验证码:")
        verification_label.pack()
        verification_entry = ttk.Entry(verification_window)
        verification_entry.pack()

        def on_verification_confirm():
            input_code = verification_entry.get()
            if self.validate_code(input_code, correct_code):
                self.add_user(username, password, email)
                messagebox.showinfo("注册成功", f"欢迎，{username}! 请使用您的新账号登录。")
                verification_window.destroy()
            else:
                messagebox.showerror("注册失败", "验证码错误！")
                verification_entry.delete(0, tk.END)  # 清空输入框

        confirm_button = ttk.Button(verification_window, text="验证", command=on_verification_confirm)
        confirm_button.pack()


def add_user(self, username, password, email):
    wb = self.init_user_excel()
    ws = wb.active
    ws.append([username, password, email])  # 假设 Excel 文件有三列：用户名、密码和邮箱
    wb.save(self.user_file)
