from django.core.mail import EmailMultiAlternatives

# 授权码wcxujgerytwadbjb
send_email = "1970255829@qq.com"


def send_mail(theme, message, receiver_mails, file=None, file_name=None):
    """

    :param theme: 主题s
    :param message: 消息
    :param receiver_mails: 接收人mails list
    :param file: 附件 文件对象
    :param file_name: 文件名称
    :return:
    """
    msg = EmailMultiAlternatives(theme, message, send_email, receiver_mails)
    if file:
        print("发送文件")
        html_content = "<p>这是一封<strong>重要的报告邮件</strong>.</p>"
        msg.attach_alternative(html_content, "text/html")
        msg.attach(file_name, file.read())
    if not msg.send():
        send_mail(theme, message, receiver_mails, file, file_name)
