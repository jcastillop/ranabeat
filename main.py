import time
from time import sleep
from process import processResend
from helpers import manageFile

#chanel_from = 1784783316 #TITIHENRY
#chanel_from = 1675076148 #TITIHENRY LATENIGHT
#chanel_to = 'Pruebas RanaBeat'
# tipos de emisores : true: chanel, false : chat
class itemTask():
    def __init__(self,chanel_from, chanel_type,chanel_to):
        self.chanel_from = chanel_from
        self.chanel_type = chanel_type
        self.chanel_to = chanel_to

arr_task = [itemTask(1784783316, True, 'Pruebas RanaBeat'), itemTask(1675076148, True, 'Pruebas RanaBeat'), itemTask(4019284206, False, 'Pruebas RanaBeat')]
#arr_task = [itemTask(4019284206, 'Pruebas RanaBeat')]

def executeTask():
    for item in arr_task:
        manageFile(item.chanel_from)
        processResend(item.chanel_from, item.chanel_type, item.chanel_to)

while True:
    print("Start: %s" % time.ctime())
    executeTask()
    sleep(45)



    



