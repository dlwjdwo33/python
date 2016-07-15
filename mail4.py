# -*- coding:utf-8 -*-
import codecs
import random
import threading
import smtplib
import logging
import sys
import email
from emaildata.text import Text
from email.mime.text import MIMEText
import time
import datetime

log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)


def randstring(length=10):
    valid_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join((random.choice(valid_letters) for i in xrange(length)))


sender = randstring()
receiver = ['test0001@alpha.terracetech.co.kr', 'test0002@alpha.terracetech.co.kr', 'test0003@alpha.terracetech.co.kr',
            'test0004@alpha.terracetech.co.kr', 'test0005@alpha.terracetech.co.kr', 'test0006@alpha.terracetech.co.kr',
            'test0007@alpha.terracetech.co.kr', 'test0008@alpha.terracetech.co.kr', 'test0009@alpha.terracetech.co.kr']

fp = codecs.open("C:\\textfile2.eml", 'rb', 'utf-8')
message = MIMEText(fp.read())
fp.close()

message["From"] = randstring()
message["To"] = 'test0012@alpha.terracetech.co.kr'

content = email.message_from_file(open("C:\\textfile2.eml"))
text = Text.text(content)
html = Text.html(content)

mailserver = raw_input("메일서버를 입력하세요 :")
count = input("스레드 갯수를 입력하세요 :")
opertime = input("실행시간을 입력하세요 : ")

startnowtime = datetime.datetime.now()
finishtime = startnowtime + datetime.timedelta(seconds=opertime)


class SendMail(threading.Thread):
    def __init__(self, fro, to, subject, contents):
        threading.Thread.__init__(self)
        self.fro = fro
        self.to = to
        self.subject = subject
        self.contents = contents

    def run(self):
        while True:

            nowtime = datetime.datetime.now()
        if (finishtime.strftime('%Y-%m-%d %H:%M:%S') == nowtime.strftime('%Y-%m-%d %H:%M:%S')):
            print '시간종료.'
            break
            server = smtplib.SMTP(mailserver, 25)
            server.sendmail(self.fro, self.to, self.contents)
            log.info("Mail transfer success")
            server.quit()


for thread in range(count):
    thread = SendMail(message["From"], message["To"], message['Subject'], html)
    thread.start()
    print thread
