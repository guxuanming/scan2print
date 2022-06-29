import time
import requests
import os
import datetime
import win32api
import win32print
import win32gui
from win32con import WM_INPUTLANGCHANGEREQUEST


def change_language(lang="EN"):
    LANG = {
        "ZH": 0x0804,
        "EN": 0x0409
    }
    hwnd = win32gui.GetForegroundWindow()
    language = LANG[lang]
    result = win32api.SendMessage(
        hwnd,
        WM_INPUTLANGCHANGEREQUEST,
        0,
        language
    )
    if not result:
        return True
    

def download_and_print(url):
    filename = "print.pdf"
    if os.path.exists(filename):
        os.remove(filename)
    response = requests.get(url, allow_redirects=True)
    open(filename, 'wb+').write(response.content)
    win32api.ShellExecute(
        0,
        "print",
        filename,
        None,
        ".",
        0
    )


if __name__ == '__main__':
    num = 0
    while True:
        num = num + 1
        change_language(lang="EN")
        current_time = str(datetime.datetime.now())                                      
        scaner_input = input(f"{current_time} 第{num}次打印：等待输入\n")
        if "http://www.aaaaa/pdf.htm?code=" in scaner_input:  # 下载地址特征
            download_and_print(scaner_input)
        elif "end" in scaner_input:
            break
        else:
            print("请扫描正确的二维码，确保当前为英文输入法，并关闭大写开关。")
            
