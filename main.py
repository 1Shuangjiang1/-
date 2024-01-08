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

    login_window.mainloop()  # 开始登录窗口的事件循环


