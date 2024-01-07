# main.py
import tkinter as tk
from tkinter import ttk, messagebox
from contact_app import ContactApp

def login(app, login_window, username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    if app.login(username, password):  # 如果登录成功
        login_window.destroy()  # 关闭登录窗口
        root.deiconify()  # 显示主窗口

def register(app):
    # 创建注册窗口
    register_window = tk.Toplevel()
    register_window.title("注册账号")

    username_label = ttk.Label(register_window, text="用户名:")
    username_label.pack()
    username_entry = ttk.Entry(register_window)
    username_entry.pack()

    password_label = ttk.Label(register_window, text="密码:")
    password_label.pack()
    password_entry = ttk.Entry(register_window, show="*")
    password_entry.pack()

    email_label = ttk.Label(register_window, text="邮箱:")
    email_label.pack()
    email_entry = ttk.Entry(register_window)
    email_entry.pack()

    # 注册按钮
    confirm_button = ttk.Button(register_window, text="注册",command=lambda: app.register_user(username_entry.get(), password_entry.get(),email_entry.get()))
    confirm_button.pack()

def forgot_password(app):
    # 创建忘记密码窗口
    fp_window = tk.Toplevel()
    fp_window.title("找回密码")

    email_label = ttk.Label(fp_window, text="注册邮箱:")
    email_label.pack()
    email_entry = ttk.Entry(fp_window)
    email_entry.pack()

    code_label = ttk.Label(fp_window, text="验证码:")
    code_label.pack()
    code_entry = ttk.Entry(fp_window)
    code_entry.pack()

    new_password_label = ttk.Label(fp_window, text="新密码:")
    new_password_label.pack()
    new_password_entry = ttk.Entry(fp_window, show="*")
    new_password_entry.pack()

    def send_code(app, email, code_entry):
        # 发送验证码并在界面上显示
        reset_code = app.send_reset_code(email)
        print("验证码已发送到邮箱:", email, "验证码:", reset_code)

    # 发送验证码按钮
    send_code_button = ttk.Button(fp_window, text="发送验证码", command=lambda: send_code(app, email_entry.get(), code_entry))
    send_code_button.pack()

    # 确认按钮
    confirm_button = ttk.Button(fp_window, text="确认", command=lambda: confirm_reset(app, email_entry.get(), code_entry.get(), new_password_entry.get(), fp_window))
    confirm_button.pack()



def send_code(app, email):
    # 发送验证码
    reset_code = app.send_reset_code(email)
    print("验证码已发送到邮箱:", email, "验证码:", reset_code)

def confirm_reset(app, email, input_code, new_password, window):
    # 校验验证码并重置密码
    if input_code == app.latest_forget_verification_code:  # 这里比对用户输入的验证码和最新发送的验证码
        app.reset_password(email, new_password)
        window.destroy()
        messagebox.showinfo("成功", "密码已重置。")
    else:
        messagebox.showerror("错误", "验证码不正确，请重新输入。")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # 先隐藏主窗口
    app = ContactApp(root)

    # 创建登录窗口
    login_window = tk.Toplevel()
    login_window.title("登录")
    username_label = ttk.Label(login_window, text="用户名:")
    username_label.pack()
    username_entry = ttk.Entry(login_window)
    username_entry.pack()
    password_label = ttk.Label(login_window, text="密码:")
    password_label.pack()
    password_entry = ttk.Entry(login_window, show="*")
    password_entry.pack()
    login_button = ttk.Button(login_window, text="登录", command=lambda: login(app, login_window, username_entry, password_entry))
    login_button.pack()

    register_button = ttk.Button(login_window, text="注册账号", command=lambda: register(app))
    register_button.pack()

    fp_button = ttk.Button(login_window, text="忘记密码？", command=lambda: forgot_password(app))
    fp_button.pack()

    login_window.mainloop()  # 开始登录窗口的事件循环


