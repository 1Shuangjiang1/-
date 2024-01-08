import tkinter as tk
from tkinter import ttk
from xpinyin import Pinyin
from ContactBook_class import *
#本文件是加减修改和筛选联系人，以及文本框展示内容设置

class admd:
    def add_contact(self):
        # 创建增加联系人的窗口
        add_window = tk.Toplevel(self.root)
        add_window.title("增加联系人")
        add_window.geometry("600x400")

        # 下拉框选择联系人类型
        contact_types = ["学生", "同事", "老师", "朋友", "亲戚"]
        type_label = ttk.Label(add_window, text="选择联系人类型:")
        type_label.pack()
        contact_type = ttk.Combobox(add_window, values=contact_types)
        contact_type.pack()

        # 姓名、生日、电话号码、邮件地址输入框
        name_label = ttk.Label(add_window, text="姓名:")
        name_label.pack()
        name_entry = ttk.Entry(add_window)
        name_entry.pack()

        birthday_label = ttk.Label(add_window, text="生日:（输入生日请按照YYYY-MM-DD）")
        birthday_label.pack()
        birthday_entry = ttk.Entry(add_window)
        birthday_entry.pack()

        phone_label = ttk.Label(add_window, text="电话号码:")
        phone_label.pack()
        phone_entry = ttk.Entry(add_window)
        phone_entry.pack()

        email_label = ttk.Label(add_window, text="邮件地址:")
        email_label.pack()
        email_entry = ttk.Entry(add_window)
        email_entry.pack()

        # 根据联系人类型显示特殊信息输入框
        def show_extra_fields():
            selected_type = contact_type.get()
            if selected_type == "学生":
                college_label = ttk.Label(add_window, text="学院:")
                college_label.pack()
                college_entry = ttk.Entry(add_window)
                college_entry.pack()

                major_label = ttk.Label(add_window, text="专业:")
                major_label.pack()
                major_entry = ttk.Entry(add_window)
                major_entry.pack()

            if selected_type == "老师":
                college_label1 = ttk.Label(add_window, text="学院:")
                college_label1.pack()
                college_entry1 = ttk.Entry(add_window)
                college_entry1.pack()

                title_label = ttk.Label(add_window, text="职称:")
                title_label.pack()
                title_entry = ttk.Entry(add_window)
                title_entry.pack()

                ResearchDirection_label = ttk.Label(add_window, text="研究方向:")
                ResearchDirection_label.pack()
                ResearchDirection_entry = ttk.Entry(add_window)
                ResearchDirection_entry.pack()

            if selected_type == "同事":
                company_label = ttk.Label(add_window, text="公司:")
                company_label.pack()
                company_entry = ttk.Entry(add_window)
                company_entry.pack()

            if selected_type == "朋友":
                howmet_label = ttk.Label(add_window, text="如何认识:")
                howmet_label.pack()
                howmet_entry = ttk.Entry(add_window)
                howmet_entry.pack()

            if selected_type == "亲戚":
                relationship_label = ttk.Label(add_window, text="亲戚关系:")
                relationship_label.pack()
                relationship_entry = ttk.Entry(add_window)
                relationship_entry.pack()

            def create_contact():
                # 创建联系人对象并添加到通讯录列表
                selected_type = contact_type.get()

                name = name_entry.get()
                birthday = birthday_entry.get()
                phone_number = phone_entry.get()
                email = email_entry.get()

                if selected_type == "学生":
                    college = college_entry.get()
                    major = major_entry.get()
                    contact = Classmate(name, birthday, phone_number, email, college, major)

                if selected_type == "老师":
                    college = college_entry1.get()
                    title = title_entry.get()
                    ResearchDirection = ResearchDirection_entry.get()
                    contact = Teacher(name, birthday, phone_number, email, college, title, ResearchDirection)

                if selected_type == "同事":
                    company = company_entry.get()
                    contact = Colleague(name, birthday, phone_number, email, company)

                if selected_type == "朋友":
                    howmet = howmet_entry.get()
                    contact = Friend(name, birthday, phone_number, email, howmet)

                if selected_type == "亲戚":
                    relationship = relationship_entry.get()
                    contact = Relative(name, birthday, phone_number, email, relationship)

                self.contacts.append(contact)
                write_user_to_file(contact, "contacts.txt")
                add_window.destroy()
                self.update_info_text()

            create_button = ttk.Button(add_window, text="创建联系人", command=create_contact)
            create_button.pack()

        # 创建联系人按钮
        create_button = ttk.Button(add_window, text="其他细节", command=show_extra_fields)
        create_button.pack()

    def del_contact(self):
        del_window = tk.Toplevel(self.root)
        del_window.title("删除联系人")
        del_window.geometry("600x400")

        contact_names = [contact.name for contact in self.contacts]
        type_label = ttk.Label(del_window, text="选择删除的联系人:")
        type_label.pack()
        contact_type = ttk.Combobox(del_window, values=contact_names)
        contact_type.pack()

        def delete_contact():
            selected_contact = contact_type.get()
            delete_user_from_file(selected_contact, "contacts.txt")
            for contact in self.contacts:
                if contact.name == selected_contact:
                    self.contacts.remove(contact)
                    break
            del_window.destroy()
            self.update_info_text()

        del_button = ttk.Button(del_window, text="确认删除", command=delete_contact)
        del_button.pack()


    def mod_contact(self):
        mod_window = tk.Toplevel(self.root)
        mod_window.title("修改联系人信息")
        mod_window.geometry("600x400")

        mod_names = [contact.name for contact in self.contacts]
        type_label = ttk.Label(mod_window, text="选择要修改信息的联系人:")
        type_label.pack()
        contact_type = ttk.Combobox(mod_window, values=mod_names)
        contact_type.pack()

        type_label = ttk.Label(mod_window, text="请输入要修改的信息:")
        type_label.pack()

        name_label = ttk.Label(mod_window, text="姓名:")
        name_label.pack()
        name_entry = ttk.Entry(mod_window)
        name_entry.pack()

        birthday_label = ttk.Label(mod_window, text="生日:")
        birthday_label.pack()
        birthday_entry = ttk.Entry(mod_window)
        birthday_entry.pack()

        phone_label = ttk.Label(mod_window, text="电话号码:")
        phone_label.pack()
        phone_entry = ttk.Entry(mod_window)
        phone_entry.pack()

        email_label = ttk.Label(mod_window, text="邮件地址:")
        email_label.pack()
        email_entry = ttk.Entry(mod_window)
        email_entry.pack()

        def modify_contact():
            selected_contact = contact_type.get()
            selected_contact = self.contacts[mod_names.index(selected_contact)]
            if name_entry.get() != "":
                initial_name = selected_contact.name
                selected_contact.name = name_entry.get()
            if birthday_entry.get() != "":
                selected_contact.birthday = birthday_entry.get()

            if phone_entry.get() != "":
                selected_contact.phone_number = phone_entry.get()

            if email_entry.get() != "":
                selected_contact.email = email_entry.get()
            print(type(selected_contact.name))
            modify_data("contacts.txt", initial_name,f"{name_entry.get()},{phone_entry.get()},{selected_contact.__class__.__name__}")
            mod_window.destroy()
            self.update_info_text()

        modi_button = ttk.Button(mod_window, text="确认修改", command=modify_contact)
        modi_button.pack()

    def display_contacts(self):
        display_window = tk.Toplevel(self.root)
        display_window.title("显示联系人")
        display_window.geometry("600x400")

        # 下拉框选择类别
        categories = ["全部", "Classmate", "Teacher", "Colleague", "Friend", "Relative"]
        category_label = ttk.Label(display_window, text="选择类别:")
        category_label.pack()
        category_combobox = ttk.Combobox(display_window, values=categories)
        category_combobox.pack()

        # 输入框选择首字母
        letter_label = ttk.Label(display_window, text="输入首字母:")
        letter_label.pack()
        letter_entry = ttk.Entry(display_window)
        letter_entry.pack()

        # 滑动框选择生日区间
        birthday_label = ttk.Label(display_window, text="选择生日区间(按照YYYY-MM-DD输入，可以仅输入年份或月份)")
        birthday_label.pack()

        start_date_var = tk.StringVar()
        end_date_var = tk.StringVar()

        start_date_label = ttk.Label(display_window, text="开始日期:")
        start_date_label.pack()
        start_date_entry = ttk.Entry(display_window, textvariable=start_date_var)
        start_date_entry.pack()

        end_date_label = ttk.Label(display_window, text="结束日期:")
        end_date_label.pack()
        end_date_entry = ttk.Entry(display_window, textvariable=end_date_var)
        end_date_entry.pack()

        def filter_contacts():
            selected_category = category_combobox.get()
            selected_letter = letter_entry.get().lower()
            start_date = start_date_var.get()
            end_date = end_date_var.get()

            filtered_contacts = []

            for contact in self.contacts:
                if selected_category == "全部" or contact.__class__.__name__ == selected_category or not selected_letter:
                    p = Pinyin()
                    if any('\u4e00' <= char <= '\u9fff' for char in contact.name):
                        # 如果包含中文字符，使用xpinyin获取拼音
                        pinyin_name = p.get_pinyin(contact.name, '')
                    else:
                        pinyin_name = contact.name
                    if selected_letter == "" or pinyin_name.lower().startswith(selected_letter):
                        if not start_date and not end_date:
                            filtered_contacts.append(contact)
                        elif not start_date:
                            if contact.birthday <= end_date:
                                filtered_contacts.append(contact)
                        elif not end_date:
                            if contact.birthday >= start_date:
                                filtered_contacts.append(contact)
                        else:
                            if start_date <= contact.birthday <= end_date:
                                filtered_contacts.append(contact)

            self.update_info_text(filtered_contacts)
            display_window.destroy()
        filter_button = ttk.Button(display_window, text="筛选", command=filter_contacts)
        filter_button.pack()



    def update_info_text(self):
        # 清空信息框并更新显示通讯录中的联系人信息
        self.info_text.delete(1.0, tk.END)
        for contact in self.contacts:
            contact_info = str(contact)
            print(contact_info)
            # 使用变量连接的方式来构建要显示的字符串
            contact_info = (
                f"Name: {contact.name}\n"
                f"Birthday: {contact.birthday}\n"
                f"Phone: {contact.phone_number}\n"
                f"Email: {contact.email}\n"
            )

            # 根据联系人类型添加额外的信息
            if isinstance(contact, Classmate):
                contact_info += f"College: {contact.college}\nMajor: {contact.major}\n"
            elif isinstance(contact, Teacher):
                contact_info += f"College: {contact.college}\nTitle: {contact.title}\nResearch Direction: {contact.ResearchDirection}\n"
            elif isinstance(contact, Colleague):
                contact_info += f"Company: {contact.company}\n"
            elif isinstance(contact, Friend):
                contact_info += f"How Met: {contact.how_met}\n"
            elif isinstance(contact, Relative):
                contact_info += f"Relationship: {contact.relationship}\n"

            contact_info += "\n"  # 在每个联系人信息的最后添加一个额外的换行符来分隔

            self.info_text.insert(tk.END, contact_info)  # 将信息插入到文本框
