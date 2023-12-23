from pathlib import Path
from datetime import datetime, timedelta
import os
import params

def getLastId(chanel_id):
    last_id = 0
    file = open('.\\'+ str(chanel_id) + '.\\' + str(chanel_id) + params.id_file, encoding="utf-8")
    try:
        last_id = int(file.read())
    except ValueError:
        writeError(chanel_id, "Error al convertir el last_id a entero, archivo corrupto")
    file.close()
    return last_id

def updateLastId(chanel_id, new_chat_id):
    writeTXTFile('.\\'+ str(chanel_id) + '.\\' + str(chanel_id) + params.id_file, new_chat_id)

def writeLog(chanel_id, message):
    now = datetime.now()
    dat = now.strftime("%d/%m/%Y %H:%M:%S") + "\t"
    appendTXTFile('.\\'+ str(chanel_id) + '.\\' + str(chanel_id) + params.log_file, dat + str(message))

def writeError(chanel_id, message):    
    now = datetime.now()
    dat = now.strftime("%d/%m/%Y %H:%M:%S") + "\t"
    appendTXTFile('.\\'+ str(chanel_id) + '.\\' + str(chanel_id) + params.error_file, dat + str(message))

#auxiliares desscargas
async def uploadMedia(client, media):
    await client.download_media(media)

#auxiliares de manejo de ficheros
def appendTXTFile(file_storage, message):
    file = open(file_storage,"a", encoding="utf-8")
    file.write(str(message) + "\n")
    file.close()     

def writeTXTFile(file_storage, message):
    file = open(file_storage,"w+", encoding="utf-8")
    file.write(str(message))
    file.close()

#Generacion de ficheros por chat (channel_id)
def manageFile(chanel_id):
    #creacion id file
    if not os.path.exists(str(chanel_id)):
        os.makedirs(str(chanel_id))
        os.makedirs(str(chanel_id) + '\\img\\')

    file_path_id = Path('.\\'+ str(chanel_id) + '.\\' + str(chanel_id) + params.id_file)
    if not file_path_id.is_file():
        file_path_id.write_text("0")    
    #creacion log file
    file_path_log = Path('.\\'+ str(chanel_id) + '.\\' + str(chanel_id) + params.log_file)
    if not file_path_log.is_file():
        file_path_log.write_text("")        
    #creacion error file
    file_path_error = Path('.\\'+ str(chanel_id) + '.\\' + str(chanel_id) + params.error_file)
    if not file_path_error.is_file():
        file_path_error.write_text("")

#manejo de fechas
def getDateUTC(fecha):
    return fecha - timedelta(hours=5)