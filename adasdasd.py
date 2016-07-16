# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText


fp = open("C:\\textfile2.eml", 'rb')

msg = MIMEText(fp.read())
fp.close()

msg['Subject'] = 'The contents of '
msg['From'] = 'hoguma33@naver.com'
msg['To'] = 'dlwjdwo33@gmail.co.kr'

s = smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login("dlwjdwo33@gmail.co.kr", "ehd359rka")
s.sendmail('hoguma33@naver.com', 'dlwjdwo33@gmail.co.kr', msg.as_string())
s.quit()