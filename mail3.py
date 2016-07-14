# -*- coding:utf-8 -*-

import random
import threading
import smtplib
import logging
import sys
from email.mime.text import MIMEText

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

fp = open("C:\\textfile.eml", 'rb')
msg = MIMEText(fp.read())
fp.close()

msg['Subject'] = "wow"
msg['From'] = randstring()
msg['To'] = 'test0012@alpha.terracetech.co.kr'

mailserver = raw_input("메일서버를 입력하세요 :")


class SendMail(threading.Thread):
    def __init__(self, fro, to, subject, contents):
        threading.Thread.__init__(self)
        self.fro = fro
        self.to = to
        self.subject = subject
        self.contents = contents

    def run(self):
        sever = smtplib.SMTP(mailserver, 25)
        sever.sendmail(self.fro, self.to, msg.as_string())
        log.info("Mail transfer success")
        sever.quit()


for s in range(5):
    t = SendMail(msg['From'], msg['To'], msg['Subject'], msg.as_string())
    t.start();
