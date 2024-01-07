from openpyxl import Workbook
from faker import Faker
import random
import string

# 创建 Faker 对象并指定本地化为中国
fake = Faker('zh_CN')

# 生成随机密码的函数
def random_password(length=8):
    characters = string.ascii_letters + string.digits  # 只使用英文字母和数字
    return ''.join(random.choice(characters) for i in range(length))

# 初始化工作簿和表格
wb = Workbook()
ws = wb.active
ws.append(["用户名", "密码"])

# 生成 10 个用户，随机中文名和密码
for _ in range(10):
    username = fake.name()  # 生成随机中文名
    password = random_password()  # 生成随机密码
    ws.append([username, password])

# 保存工作簿
wb.save("users.xlsx")
