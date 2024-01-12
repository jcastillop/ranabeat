from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest, GetHistoryRequest
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import os
import pathlib

import params
from helpers import getLastId, updateLastId, writeLog, getDateUTC, writeError
from datetime import datetime, timedelta
from variables import appVars

def processResend(chanel_id_from, chanel_type, chanel_id_to):

    file = appVars["file"]

    print("Inicio del proceso reenvio mensajes, descarga de imagenes from: " + str(chanel_id_from))
    #writeLog("chanel_id_from: " + str(chanel_id_from) + " - INICIO 0.1")
    last_id = getLastId(chanel_id_from)
     
    with TelegramClient('name', params.api_id, params.api_hash) as client:
        entity = PeerChat(chanel_id_from)
        if chanel_type:
            entity = PeerChannel(chanel_id_from)
        channel_entity=client.get_entity(entity)
        channel_receive_entity=client.get_entity(chanel_id_to)
        posts = client(GetHistoryRequest(
            peer=channel_entity,
            limit=100,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0))
        
        while last_id != posts.messages[0].id:
            last_id += 1
            for chat in posts.messages:
                if (chat.id == last_id) or (last_id==1):
                    writeLog(str(chat.id) + "\t" + str(getDateUTC(chat.date))+ "\t" + str(chat.message))
                    try:
                        if chat.media != None:
                            client.download_media(chat.media, file["image"])
                        if chat.message:
                            client.send_message(entity=channel_receive_entity,message=chat.message)
                        #almacenar en BD
                        if last_id == 1:
                            last_id = chat.id
                            #si el archivo donde se almacena los id se acaba de crear entonces registrar el ultimo mensaje
                            break                           
                    except Exception as e:
                        writeError(e)
            #actualizar el nuevo id
            updateLastId(last_id)

            # i = 0
            # while last_id != posts.messages[i].id:
            #     chat = posts.messages[i]
            #     #dt = datetime.strptime(str(chat.date), '%Y-%m-%d %H:%M:%S')
            #     writeLog(str(chat.id) + "\t" + str(getDateUTC(chat.date))+ "\t" + str(chat.message))
            #     i += 1
            #     try:
            #         if chat.media != None:
            #             client.download_media(chat.media, file["image"])
            #         if chat.message:
            #             client.send_message(entity=channel_receive_entity,message=chat.message)
            #         #almacenar en BD
            #         if last_id == 0:
            #             #si el archivo donde se almacena los id se acaba de crear entonces registrar el ultimo mensaje
            #             break                    
            #     except Exception as e:
            #         writeError(e)

        #print("Fin del proceso reenvio mensajes, descarga de imagenes from: " + str(chanel_id_from))
        #writeLog("Fin del proceso chanel_id_from: " + str(chanel_id_from) + " - FIN 0.1")
        #print("Inicio del proceso reenvio imagenes from: " + str(chanel_id_from))
        #writeLog("Inicio del proceso reenvio imagenes chanel_id_from: " + str(chanel_id_from) + " - INICIO 1.1")
        for filename in os.listdir(file["image"]):
            f = os.path.join(file["image"], filename)
            if os.path.isfile(f) and pathlib.Path(filename).suffix == '.jpg':
                client.send_file(channel_receive_entity, f)     
                writeLog(f)             
        #writeLog("Fin del proceso reenvio imagenes chanel_id: " + str(chanel_id_from) + " - FIN 1.1")
        #print("Fin del proceso reenvio imagenes from: " + str(chanel_id_from))
