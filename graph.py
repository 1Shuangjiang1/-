
from collections import Counter
import matplotlib.pyplot as plt

#这时启帆的绘图界面

def show_charts(self):
    # 统计各个类型的联系人数量
    contact_types = [contact.__class__.__name__ for contact in self.contacts]
    contact_counts = Counter(contact_types)

    # 生成饼图
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.pie(contact_counts.values(), labels=contact_counts.keys(), autopct='%1.1f%%')
    plt.title('联系人类型占比')

    # 生成条形图
    plt.subplot(1, 2, 2)
    plt.bar(contact_counts.keys(), contact_counts.values())
    plt.title('联系人类型数量')
    plt.xticks(rotation=45)

    # 显示图表
    plt.tight_layout()
    plt.show()