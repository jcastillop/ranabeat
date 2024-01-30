import time
from time import sleep
from process import processResend
from helpers import manageFile

#2104894807 canal origen
#4019284206 PRUEBAS RANA 2
#1517627668 MaX ORIGAMI
#1622772055 VICTORCONNECTION
#1784783316 TITIHENRY
#1369987187-TitiHenry⚽️
#1213735452-⛓ORIGAMI⛓
#actual produccion max origami
class itemTask():
    def __init__(self,chanel_from, chanel_type,chanel_to):
        self.chanel_from = chanel_from
        self.chanel_type = chanel_type
        self.chanel_to = chanel_to

arr_task = [
    itemTask(1517627668, True, 4019284206),
    itemTask(1622772055, True, 4019284206),
    itemTask(1784783316, True, 4019284206)
]

def executeTask():
    for item in arr_task:
        manageFile(item.chanel_from)
        processResend(item.chanel_from, item.chanel_type, item.chanel_to)

while True:
    print("Starts: %s" % time.ctime())
    executeTask()
    sleep(10)



    



