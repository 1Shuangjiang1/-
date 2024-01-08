from tkinter import messagebox
import openpyxl
import os
from ContactBook_class import *

#这时启帆的自动导入联系人界面

def toggle_auto_import(self):
    self.auto_import_enabled = not self.auto_import_enabled
    if self.auto_import_enabled:
        messagebox.showinfo("自动导入", "自动导入功能已开启。")
    else:
        messagebox.showinfo("自动导入", "自动导入功能已关闭。")


def auto_import_contacts(self):
    file_path = f"{self.username}_Contacts.xlsx"
    if os.path.exists(file_path):
        try:
            # 打开工作簿和选择工作表
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active

            # self.contacts.clear()
            # 清除当前所有联系人

            for row in sheet.iter_rows(min_row=2):
                contact_type, name, birthday, phone_number, email, extra_info = [cell.value for cell in row]

                # 根据提取的额外信息创建联系人对象
                new_contact = None
                if contact_type == '同学':
                    college, major = extra_info.split("; ")
                    new_contact = Classmate(name, birthday, phone_number, email, college, major)
                elif contact_type == '老师':
                    college, title, research_direction = extra_info.split("; ")
                    new_contact = Teacher(name, birthday, phone_number, email, college, title, research_direction)
                elif contact_type == '同事':
                    company = extra_info
                    new_contact = Colleague(name, birthday, phone_number, email, company)
                elif contact_type == '亲戚':
                    relationship = extra_info  # 对于亲戚，额外信息中只有亲戚关系的描述
                    new_contact = Relative(name, birthday, phone_number, email, relationship)
                elif contact_type == '朋友':
                    how_met = extra_info
                    new_contact = Friend(name, birthday, phone_number, email, how_met)

                if new_contact:
                    self.contacts.append(new_contact)

            self.update_info_text()  # 更新界面显示
            messagebox.showinfo("自动导入", "联系人已成功自动导入。")
        except Exception as e:
            messagebox.showerror("自动导入", f"导入失败: {e}")
