import os
import yagmail

def get_contents(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def get_emails(path):
    with open(path, 'r') as f:
        return f.read().splitlines()

def send_email(src, dst, subject, contents, attachments):
    pwd = os.environ.get('wangyi_emai_auth')

    yag = yagmail.SMTP(user=src, password=pwd, host='smtp.163.com', port='465')
    yag.send(to=dst, subject=subject, contents=contents, attachments=attachments)
    yag.close()

def send_emails(src, tos, subject, contents, attachments):
    for to in tos:
        send_email(src, to, subject, contents, attachments)  

if __name__ == "__main__":
    try:
        path = '/root/github-trending/2024-11-25.txt'
        src = '19121220286@163.com'
        tos = get_emails('emails_test.txt') 
        subject = '群发测试'
        contents = get_contents(path)
        attachments = path
        
        send_emails(src, tos, subject, contents, attachments)
    except Exception as e:
        print(f"{e} occured in job")