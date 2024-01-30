from pathlib import Path
from datetime import datetime, timedelta
import os
import params
from variables import appVars

def getLastId(chanel_id):
    file_manager = appVars["file"]
    last_id = 0
    file = open(file_manager["id"], encoding="utf-8")
    try:
        last_id = int(file.read())
    except:
        writeError(chanel_id, "Error al convertir el last_id a entero, archivo corrupto")
    finally:
        file.close()
        
    return last_id

def updateLastId(new_chat_id):
    file = appVars["file"]
    writeTXTFile(file["id"], new_chat_id)

def writeLog(message):
    file = appVars["file"]
    now = datetime.now()
    dat = now.strftime("%d/%m/%Y %H:%M:%S") + "\t"
    appendTXTFile(file["log"], dat + str(message))

def writeError(message):    
    file = appVars["file"]
    now = datetime.now()
    dat = now.strftime("%d/%m/%Y %H:%M:%S") + "\t"
    appendTXTFile(file["error"], dat + str(message))

#auxiliares desscargas
async def uploadMedia(client, media):
    await client.download_media(media)

#auxiliares de manejo de ficheros
def appendTXTFile(file_storage, message):
    try:
        file = open(file_storage,"a", encoding="utf-8")
        file.write(str(message) + "\n")
    except:
        print("Error appendTXTFile" + str(file_storage) + " con el mensaje " + message)
    finally:
        file.close()    
  

def writeTXTFile(file_storage, message):
    try:
        file = open(file_storage,"w+", encoding="utf-8")
        file.write(str(message))
    except:
        print("Error writeTXTFile" + str(file_storage) + " con el mensaje " + message)
    finally:
        file.close()       

#Generacion de ficheros por chat (channel_id)
def manageFile(chanel_id):

    try:
        file = appVars["file"]

        now = datetime.now()
        dat = now.strftime("%Y%m%d")
        #creacion id file
        root = 'data/' + dat + '/' + str(chanel_id)
        if not os.path.exists(root):
            os.makedirs(root)
            os.makedirs(root + '/img/')

        file["image"] = root + '/img/'

        for filename in os.listdir(file["image"]):
            if os.path.isfile(os.path.join(file["image"], filename)):
                os.remove(os.path.join(file["image"], filename))          

        file["id"] = 'data/' + str(chanel_id) + params.id_file
        file_path_id = Path(file["id"])
        if not file_path_id.is_file():
            file_path_id.write_text("0")    
        #creacion log file
        file["log"] = root + '/' + str(chanel_id) + params.log_file
        file_path_log = Path(file["log"])
        if not file_path_log.is_file():
            file_path_log.write_text("")        
        #creacion error file
        file["error"] = root + '/' + str(chanel_id) + params.error_file
        file_path_error = Path(file["error"])
        if not file_path_error.is_file():
            file_path_error.write_text("")
    except:
        print("Error manageFile")



#manejo de fechas
def getDateUTC(fecha):
    return fecha - timedelta(hours=5)