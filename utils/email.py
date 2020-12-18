from django.core import mail

# 授权码wcxujgerytwadbjb
from_email = "1970255829@qq.com"


def send_mail(theme, message, receiver_mails):
    mail.send_mail(theme, message, from_email, receiver_mails)
