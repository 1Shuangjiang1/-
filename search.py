import tkinter as tk
from tkinter import ttk

#这是查询功能

def create_search_gui(self):
    # 创建一个新窗口来进行查询
    search_window = tk.Toplevel(self.root)
    search_window.title("联系人查询")

    # 创建查询条件的输入框
    self.name_entry = self.create_search_entry(search_window, '姓名:')
    self.birthday_entry = self.create_search_entry(search_window, '生日:')
    self.phone_entry = self.create_search_entry(search_window, '电话:')
    self.email_entry = self.create_search_entry(search_window, '电子邮件:')

    # 创建查询按钮
    search_button = ttk.Button(search_window, text="查询", command=self.simple_search)
    search_button.pack()


def create_search_entry(self, parent, label_text):
    label = ttk.Label(parent, text=label_text)
    label.pack()
    entry = ttk.Entry(parent)
    entry.pack()
    return entry


def simple_search(self):
    name = self.name_entry.get().strip().lower()
    birthday = self.birthday_entry.get().strip().lower()
    phone = self.phone_entry.get().strip().lower()
    email = self.email_entry.get().strip().lower()

    # 过滤匹配的联系人
    results = [contact for contact in self.contacts if
               (not name or name in contact.name.lower()) and
               (not birthday or birthday in contact.birthday.lower()) and
               (not phone or phone in contact.phone_number.lower()) and
               (not email or email in contact.email.lower())]

    # 在这里处理查询结果，例如展示在界面上等
    self.display_search_results(results)


def display_search_results(self, results):
    # 清空之前的查询结果
    self.info_text.delete('1.0', tk.END)

    # 将查询结果显示在信息框中
    for contact in results:
        self.info_text.insert(tk.END,
                              f"{contact.name}, {contact.birthday}, {contact.phone_number}, {contact.email}\n")