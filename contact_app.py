from ContactBook_class import *
import tkinter as tk
from tkinter import ttk
from xpinyin import Pinyin
from openpyxl import Workbook
from openpyxl import load_workbook

def write_user_to_file(user, filename):
    with open(filename, 'a') as file:
        file.write(f"{user.name},{user.phone_number},{user.__class__.__name__}\n")

def read_users_from_file(filename):
    users = []
    with open(filename, 'r') as file:
        for line in file:
            name, phone_number, user_type = line.strip().split(',')
            if user_type == 'Classmate':
                user = Classmate(name,1 ,phone_number,1,1,1)
            elif user_type == 'Teacher':
                user = Teacher(name, 1,phone_number,1,1,1,1)
            elif user_type == 'Colleague':
                user = Colleague(name,1, phone_number,1,1)
            elif user_type == 'Friend':
                user = Friend(name, 1,phone_number,1,1)
            elif user_type == 'Relative':
                user = Relative(name, 1,phone_number,1,1)
            users.append(user)
    return users

def delete_user_from_file(username, filename):
    # Read all users from the file
    users = read_users_from_file(filename)

    # Find the user with the specified name
    users = [user for user in users if user.name != username]

    # Rewrite the updated user list to the file
    with open(filename, 'w') as file:
        for user in users:
            file.write(f"{user.name},{user.phone_number},{user.__class__.__name__}\n")

def modify_data(filename, target_name, new_data):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            # Assuming the name is in the first column
            if line.split(',')[0].strip() == target_name:
                # Modify the line with new data
                lines[i] = f"{new_data}\n"

        with open(filename, 'w') as file:
            file.writelines(lines)
class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("通讯录")
        self.contacts = []
        self.create_gui()

    def create_gui(self):
        # 创建增加联系人按钮
        add_button = ttk.Button(self.root, text="增加联系人", command=self.add_contact)
        add_button.pack()

        # 创建删除联系人按钮
        del_button = ttk.Button(self.root, text="删除联系人", command=self.del_contact)
        del_button.pack()

        mod_button = ttk.Button(self.root, text="修改联系人信息", command=self.mod_contact)
        mod_button.pack()

        sort_button = ttk.Button(self.root, text="按生日排序", command=self.sort_contacts_by_birthday)
        sort_button.pack()

        display_button = ttk.Button(self.root, text="显示联系人", command=self.display_contacts)
        display_button.pack()
        sort_by_surname_button = ttk.Button(self.root, text="按姓氏排序", command=self.sort_contacts_by_surname)
        sort_by_surname_button.pack()

        # root = tk.Tk()
        # root.title("通讯录")
        #
        # # 创建 Text 组件，设置字体
        # font = ("微软雅黑", 12)
        # info_text = tk.Text(root, height=10, width=30, font=font)
        # info_text.pack()

        table_button = ttk.Button(self.root, text="显示联系人表格", command=self.display_table)
        table_button.pack()

        export_button = ttk.Button(self.root, text="导出到Excel", command=self.export_to_excel)
        export_button.pack()

        import_button = ttk.Button(self.root, text="导入联系人", command=self.import_from_excel)
        import_button.pack()

        simple_search_button = ttk.Button(self.root, text="简化查询", command=self.create_search_gui)
        simple_search_button.pack()

        #创建信息框来显示联系人姓名
        self.info_text = tk.Text(self.root, height=10, width=30)
        self.info_text.pack()

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
                write_user_to_file(contact,"contacts.txt")
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

    def sort_contacts_by_birthday(self):
        # 对联系人按生日排序，假设生日格式为YYYY-MM-DD
        self.contacts.sort(key=lambda x: x.birthday)
        self.update_info_text()  # 更新信息框以显示排序后的联系人
    
    def sort_contacts_by_surname(self):
        # 对联系人按照姓名的拼音进行排序
        p = Pinyin()
        self.contacts.sort(key=lambda x: p.get_pinyin(x.name, ''))
        self.update_info_text()  # 更新信息框以显示排序后的联系人

    
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
            table.insert("", tk.END, values=(contact.name, contact.birthday, contact.phone_number, contact.email, extra_info))

        # 放置表格
        table.pack(expand=True, fill='both')

        # 启动窗口循环
        table_window.mainloop()

    def export_to_excel(self):
        # 创建一个Excel工作簿
        workbook = Workbook()
        sheet = workbook.active

        # 添加表头
        headers = ["姓名", "生日", "电话", "电子邮件", "额外信息"]
        sheet.append(headers)

        # 遍历联系人，添加到表格中
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

            # 将每个联系人的信息作为一行添加到表格中
            sheet.append([contact.name, contact.birthday, contact.phone_number, contact.email, extra_info])

        # 保存工作簿到文件
        workbook.save(filename="Contacts.xlsx")

    def import_from_excel(self):
        # 定义Excel文件的路径
        excel_path = "Contacts.xlsx"  # 请确保这个路径和文件名与你之前保存的Excel文件匹配

        # 打开工作簿和选择工作表
        workbook = load_workbook(excel_path)
        sheet = workbook.active

        # 清除当前所有联系人
        self.contacts.clear()

        # 从第二行开始遍历（假设第一行是标题行）
        for row in sheet.iter_rows(min_row=2):
            name = row[0].value
            birthday = row[1].value
            phone_number = row[2].value
            email = row[3].value
            extra_info = row[4].value  # 你需要根据extra_info的内容适当解析并创建相应的联系人对象

            # 创建联系人对象并添加到列表
            # 这里假设所有的联系人都是Classmate类型，你需要根据extra_info来创建正确类型的联系人
            new_contact = Classmate(name, birthday, phone_number, email, "CollegeName", "MajorName")
            self.contacts.append(new_contact)

        # 更新显示或其他操作
        self.update_info_text()

    def create_search_gui(self):
        # 创建一个新窗口来进行查询
        search_window = tk.Toplevel(self.root)
        search_window.title("简化查询")

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

