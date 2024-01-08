from tkinter import ttk
import tkinter as tk
#本文件是ui界面所有按钮设定
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

    stats_button = ttk.Button(self.root, text="显示统计图表", command=self.show_charts)
    stats_button.pack()

    exit_button = ttk.Button(self.root, text="退出并保存", command=self.exit_app)
    exit_button.pack()

    table_button = ttk.Button(self.root, text="显示联系人表格", command=self.display_table)
    table_button.pack()

    export_button = ttk.Button(self.root, text="导出到Excel", command=self.export_to_excel)
    export_button.pack()

    import_button = ttk.Button(self.root, text="导入联系人", command=self.import_from_excel)
    import_button.pack()

    simple_search_button = ttk.Button(self.root, text="简化查询", command=self.create_search_gui)
    simple_search_button.pack()

    self.auto_import_button = ttk.Checkbutton(self.root, text="启用自动导入联系人", command=self.toggle_auto_import)
    self.auto_import_button.pack()

    # 创建信息框来显示联系人姓名
    self.info_text = tk.Text(self.root, height=10, width=30)
    self.info_text.pack()