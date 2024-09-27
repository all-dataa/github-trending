import os
import yagmail
def get_contents(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
def send_email(src, dst, subject, body):
    src = src
    pwd = os.environ.get('wangyi_emai_auth')

    yag = yagmail.SMTP(user=src, password=pwd, host='smtp.163.com', port='465')
    yag.send(to=dst, subject=subject, contents=body)
    yag.close()

def send_emails(src, tos, subject, body):
    for to in tos:
        send_email(src, to, subject, body)  

if __name__ == '__main__':
    src = '19121220286@163.com'
    tos = ['pxxhl@qq.com', 'hsh-me@outlook.com']
    to = 'pxxhl@qq.com'
    subject = '每日 github 趋势项目'
    path = 'D:\\github trending\\2024-09-27.md'
    contents = ['这里是邮件正文', get_contents(path), path]
    
    send_emails(src, tos, subject, contents)