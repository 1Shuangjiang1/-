from function.sort_bir_and_surname import *
from function.ver_code_and_reg import *
from function.graph import *
from function.create_excel import *
from function.add_del_mod_dis import admd
from function.creat_gui import create_gui
from function.login_zhengli import loglogin
from function.display import *
from function.search import *
import matplotlib.pyplot as plt
from function.auto_import_contacts import *
from tkinter import messagebox


plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统使用SimHei字体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

class ContactApp(loglogin) :
    def __init__(self, root):
        self.root = root
        self.root.title("通讯录")
        self.contacts = []
        self.create_gui()
        self.user_file = "users.xlsx"
        self.blacklist_file = "blacklist.xlsx"
        self.username = None
        self.auto_import_enabled = True
        self.email = None  # 邮箱属性

    #UI界面设计
    def create_gui(self):
        create_gui(self)
    #添加，删除，更改，筛选并展示展示联系人信息，更新文本框
    def add_contact(self):
        admd.add_contact(self)
    def del_contact(self):
        admd.del_contact(self)
    def mod_contact(self):
        admd.mod_contact(self)
    def display_contacts(self):
        admd.display_contacts(self)

    def update_info_text(self):
        admd.update_info_text(self)

    #排序
    def sort_contacts_by_birthday(self):
        sort_contacts_by_birthday(self)
    def sort_contacts_by_surname(self):
        sort_contacts_by_surname(self)

    #展示
    def display_table(self):
        display_table(self)

    #excel表格的写入与读入
    def export_to_excel(self):
        export_to_excel(self)
    def import_from_excel(self, file_path=None):
        import_from_excel(self, file_path=None)
    def create_contact_from_excel(self, contact_type, name, birthday, phone_number, email, extra_info):
        create_contact_from_excel( self, contact_type, name, birthday, phone_number, email, extra_info)

    #查询
    def create_search_gui(self):
        create_search_gui(self)

    def create_search_entry(self, parent, label_text):
        create_search_entry(self, parent, label_text)

    def simple_search(self):
        simple_search(self)

    def display_search_results(self, results):
        display_search_results(self, results)


    #图表
    def show_charts(self):
       show_charts(self)

    #保存并退出
    def exit_app(self):
        if messagebox.askokcancel("退出", "您确定要退出并保存联系人吗？"):
            # 调用修改后的export_to_excel方法
            self.export_to_excel()
            self.root.destroy()
   #自动导入联系人
    def toggle_auto_import(self):
        toggle_auto_import(self)

    def auto_import_contacts(self):
       auto_import_contacts(self)


    def generate_random_code(self,length=6):
        generate_random_code(self, length=6)
    def send_verification_code(self, email):
        send_verification_code(self, email)

    def validate_code(self, input_code, correct_code):
        validate_code(self, input_code, correct_code)

    def register_user(self, username, password, email):
        register_user(self, username, password, email)
    def add_user(self, username, password, email):
        add_user(self, username, password, email)




