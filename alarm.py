import ctypes, playsound
import sys
from win10toast import ToastNotifier
import winsound
import datetime
import time


duration = 100
freq = 1000

toaster = ToastNotifier()
#toaster.show_toast("Timer!!!", "Love your work!", duration=5)
'''while 1:
    t=datetime.datetime.now().time()
    x=datetime.time(2,25,50)
    if x < t:
        toaster.show_toast("Get up!")
        break

'''
#playsound.playsound('H:\\TaareZameenPar.mp3', False)
while 1:
    #toaster.show_toast("Relax!!!", "Python is awesome!", duration=10)
    for remaining in range(3000, 0, -1):
        if remaining%60 == 0:
        	sys.stdout.write("\r")
        	sys.stdout.write("{:2d} minutes remaining.".format(remaining//60))
        	sys.stdout.flush()
        time.sleep(1)
    playsound.playsound('H:\TaareZameenPar.mp3', False)
    for remaining in range(600, 0, -1):
        if remaining % 60 ==0:
        	sys.stdout.write("\r")
        	sys.stdout.write("{:2d} minutes remaining.".format(remaining//60))
        	sys.stdout.flush()
        time.sleep(1)
    toaster.show_toast("Hello World!!!", "Get Back to Work", duration=10)
    sys.stdout.write("\r50 Minutes done            \n")
    sys.stdout.flush()
    