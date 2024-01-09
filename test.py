def send_verification_code_to_email(self, email):
    # 生成验证码
    self.current_verification_code = self.generate_random_code(6)
    # 发送邮件
    mail_title = '继承联系人验证码'
    mail_content = f'您的验证码是：{self.current_verification_code}'
    send_verification_email(self.host_server, self.sender_qq, self.pwd, email, mail_title, mail_content)
    print(f"验证码 {self.current_verification_code} 已发送到邮箱 {email}")


def generate_random_code(self, length=6):
    """生成一个指定长度的随机验证码，包含数字和字母。"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))


def add_inherited_contacts_with_verification(self, other_username, other_password, email, input_code, window):
    if self.validate_other_user(other_username, other_password):
        if input_code == self.current_verification_code:
            other_contacts = self.read_other_user_contacts(other_username)
            # ...添加到当前用户的联系人列表...
            messagebox.showinfo("成功", "联系人已继承！")
            window.destroy()
        else:
            messagebox.showerror("错误", "验证码错误。")
    else:
        messagebox.showerror("错误", "用户名或密码错误。")