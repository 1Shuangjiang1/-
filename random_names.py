from openpyxl import Workbook
import random
from faker import Faker

# 创建 Faker 对象，用于生成数据，设置为中文
fake = Faker('zh_CN')


# 定义一个函数来创建一个随机的联系人信息
def create_random_contact():
    name = fake.name()  # 生成中文名字
    birthday = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=65).strftime('%Y-%m-%d')
    phone_number = fake.phone_number()
    email = fake.email()

    # 定义额外信息
    college = f"{fake.word()}大学"
    major = f"{fake.word()}学"
    title = random.choice(["讲师", "副教授", "教授", "助教"])
    research_direction = f"{fake.sentence(nb_words=6)}"
    company = fake.company()
    how_met = f"{fake.sentence(nb_words=6)}"
    relationship = random.choice(["表弟", "表姐", "堂兄", "堂妹"])

    # 随机选择联系人的类型，并生成相应的额外信息
    contact_type = random.choice(['同学', '老师', '同事', '朋友', '亲戚'])
    extra_info = ''
    if contact_type == '同学':
        extra_info = f"{college}; {major}"
    elif contact_type == '老师':
        extra_info = f"{college}; {title}; {research_direction}"
    elif contact_type == '同事':
        extra_info = f"{company}"
    elif contact_type == '朋友':
        extra_info = f"{how_met}"
    elif contact_type == '亲戚':
        extra_info = f"{relationship}"

    return [contact_type, name, birthday, phone_number, email, extra_info]


# 创建 Excel 工作簿和工作表
wb = Workbook()
ws = wb.active

# 添加标题行
titles = ["类别", "姓名", "生日", "电话", "电子邮件", "额外信息"]
ws.append(titles)

# 生成50个联系人并添加到工作表
for _ in range(50):
    contact = create_random_contact()
    ws.append(contact)

# 保存工作簿
filename = 'RandomContactsFormatted.xlsx'
# filename = '朱玉兰_Contacts.xlsx'
wb.save(filename)