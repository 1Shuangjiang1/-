"""
实现自动发送消息
"""

import time
import os
from pywinauto.keyboard import send_keys  # 键盘

while True:
    time_now = time.strftime("%H:%M:%S", time.localtime())  # 获取当前时间
    sent_time = time.strftime("%H:%M:%S", time.localtime())  # 发送时间
    if time_now == sent_time:  # 当前时间等于发送时间则执行以下程序
        def open_app(app_dir):
            os.startfile(app_dir)


        # 打开微信
        if __name__ == "__main__":
            app_dir = r"C:\Users\Public\Desktop\微信.lnk" # 此处为微信的绝对路径
            open_app(app_dir)
            time.sleep(1)

        # 进入微信，模拟按键Ctrl+F
        send_keys('^f')
        send_keys('文件传输助手')
        time.sleep(1)
        send_keys('{ENTER}')  # 回车键必须全部大小

        # 需要发送的消息内容
        message = '啦啦！！，是时候休息啦！Good night！！！'
        time.sleep(1)

        # 输入聊天内容
        send_keys(message)
        # 回车发送消息
        send_keys('{ENTER}')

        time.sleep(3)
        print('退出~~~')

        exit()  # 退出程序



