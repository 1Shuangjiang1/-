import tkinter as tk
from tkinter import ttk
from ContactBook_class import *
#本文件是联系人展示
def display_table(self):
    # 创建一个新窗口来显示表格
    table_window = tk.Toplevel(self.root)
    table_window.title("联系人表格")

    # 创建一个Treeview控件
    columns = ("name", "birthday", "phone", "email", "extra")
    table = ttk.Treeview(table_window, columns=columns, show='headings')

    # 定义列标题
    table.heading("name", text="姓名")
    table.heading("birthday", text="生日")
    table.heading("phone", text="电话")
    table.heading("email", text="电子邮件")
    table.heading("extra", text="额外信息")

    # 添加联系人到表格中
    for contact in self.contacts:
        extra_info = ''
        if isinstance(contact, Classmate):
            extra_info = f"学院: {contact.college}, 专业: {contact.major}"
        elif isinstance(contact, Teacher):
            extra_info = f"学院: {contact.college}, 职称: {contact.title}, 研究方向: {contact.ResearchDirection}"
        elif isinstance(contact, Colleague):
            extra_info = f"公司: {contact.company}"
        elif isinstance(contact, Friend):
            extra_info = f"如何认识: {contact.how_met}"
        elif isinstance(contact, Relative):
            extra_info = f"亲戚关系: {contact.relationship}"

        # 将联系人信息插入表格
        table.insert("", tk.END,
                     values=(contact.name, contact.birthday, contact.phone_number, contact.email, extra_info))

    # 放置表格
    table.pack(expand=True, fill='both')

    # 启动窗口循环
    table_window.mainloop()