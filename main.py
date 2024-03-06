import time
from time import sleep
from process import processResend
from helpers import manageFile
import asyncio

#chanel_from = 1784783316 #TITIHENRY
#chanel_from = 1675076148 #TITIHENRY LATENIGHT
#chanel_from = 1064299487 Bet2Earn Oficial
#chanel_from = 1877311653 REVENTA DYLER
#chanel_from = 1517627668 REVENTA DYLER
#chanel_to = 'Pruebas RanaBeat'
# tipos de emisores : true: chanel, false : chat
#4019284206 Pruebas ranabeat 2
#2104894807 canal origen
#chanel_from = 1784783316 #TITIHENRY

#chanel_from = 1802759467 MAX ORIGAMI
#chanel_from = 2075295985 TITIHENRY MARZO
#chanel_from = 1213588067 Formula Nacho PREMIUM

#actual produccion max origami
class itemTask():
    def __init__(self,chanel_from, chanel_type,chanel_to):
        self.chanel_from = chanel_from
        self.chanel_type = chanel_type
        self.chanel_to = chanel_to

arr_task = [
    itemTask(1802759467, True, 4019284206),
    itemTask(2075295985, True, 4019284206),
    itemTask(1213588067, True, 4019284206)
    # itemTask(2104894807, True, 4019284206)
    
]
#arr_task = [itemTask(4019284206, 'Pruebas RanaBeat')]

def executeTask():
    for item in arr_task:
        manageFile(item.chanel_from)
        asyncio.run(processResend(item.chanel_from, item.chanel_type, item.chanel_to))

while True:
    print("Starts: %s" % time.ctime())
    executeTask()
    sleep(10)



    



