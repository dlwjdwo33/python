# -*- coding:utf-8 -*-
import time, threading
import datetime, threading

def foo():
    print datetime.datetime.now()
    threading.Timer(0.01 ,foo).start()

foo()