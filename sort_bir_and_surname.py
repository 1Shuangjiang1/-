from xpinyin import Pinyin
def sort_contacts_by_birthday(self):
    # 对联系人按生日排序，假设生日格式为YYYY-MM-DD
    self.contacts.sort(key=lambda x: x.birthday)
    self.update_info_text()  # 更新信息框以显示排序后的联系人


def sort_contacts_by_surname(self):
    # 对联系人按照姓名的拼音进行排序
    p = Pinyin()
    self.contacts.sort(key=lambda x: p.get_pinyin(x.name, ''))
    self.update_info_text()  # 更新信息框以显示排序后的联系人