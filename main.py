import time
from time import sleep
from process import processResend
from helpers import manageFile

#chanel_from = 1784783316 #TITIHENRY
#chanel_from = 1675076148 #TITIHENRY LATENIGHT
#chanel_from = 1064299487 Bet2Earn Oficial
#chanel_from = 1877311653 REVENTA DYLER
#chanel_to = 'Pruebas RanaBeat'
# tipos de emisores : true: chanel, false : chat
#2029273638 Pruebas ranabeat 2
class itemTask():
    def __init__(self,chanel_from, chanel_type,chanel_to):
        self.chanel_from = chanel_from
        self.chanel_type = chanel_type
        self.chanel_to = chanel_to

arr_task = [
    itemTask(1784783316, True, 2029273638), 
    itemTask(1675076148, True, 2029273638), 
    itemTask(4019284206, False, 2029273638), 
    itemTask(1064299487, True, 2029273638),
    itemTask(1877311653, True, 2029273638)
]
#arr_task = [itemTask(4019284206, 'Pruebas RanaBeat')]

def executeTask():
    for item in arr_task:
        manageFile(item.chanel_from)
        processResend(item.chanel_from, item.chanel_type, item.chanel_to)

while True:
    print("Starts: %s" % time.ctime())
    executeTask()
    sleep(10)



    



