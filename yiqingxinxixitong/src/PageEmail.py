import smtplib
import time

# QQ邮箱

HOST = 'smtp.qq.com'  # 服务器主机,相当于第三方客户端

PORT = '465'  # 端口 使用SSL，端口号465或587

FROM = ''  # 发件人的邮箱账号
TO = ['']  # 接收邮件的人的账号.

SUBJECT = '上报疫情提醒'  # 邮件的标题

CONTENT = '请速速上报疫情'  # 邮件的内容

# 创建邮件发送对象

smtp_obj1 = smtplib.SMTP()

smtp_obj = smtplib.SMTP_SSL()

smtp_obj.connect(host=HOST, port=PORT)

res = smtp_obj.login(user=FROM, password='授权码')

print(res, '登录成功')

for to in TO:
    print(to)
    msg = '\n'.join(['From: {}'.format(FROM), 'To: {}'.format(to), 'SUBJECT:{}'.format(SUBJECT), '', CONTENT])  # 发送邮件,这里是我们按照邮箱的格式拼接一下.
    smtp_obj.sendmail(from_addr=FROM, to_addrs=[to], msg=msg.encode('utf-8'))
    print('发送成功')
