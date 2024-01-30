from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest, GetHistoryRequest
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import os
import pathlib
import re

import params
from helpers import getLastId, updateLastId, writeLog, getDateUTC, writeError
from datetime import datetime, timedelta
from variables import appVars

def processResend(chanel_id_from, chanel_type, chanel_id_to):

    file = appVars["file"]
    last_id = getLastId(chanel_id_from)
     
    with TelegramClient('name', params.api_id, params.api_hash) as client:
        entity = PeerChat(chanel_id_from)
        if chanel_type:
            entity = PeerChannel(chanel_id_from)
        channel_entity=client.get_entity(entity)
        channel_receive_entity=client.get_entity(chanel_id_to)
        posts = client(GetHistoryRequest(
            peer=channel_entity,
            limit=5,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0))
        print( "Canal: " + str(chanel_id_from) + " - ultimo identificador registrado en TXT: " + str(last_id) )
        while last_id != posts.messages[0].id:
            print( "Chat nuevo encontrado con id: " + str(posts.messages[0].id))
            last_id += 1
            for chat in posts.messages:
                print( "Evaluando el id: " + str(last_id))
                if (chat.id == last_id) or (last_id==1):
                    writeLog(str(chat.id) + "\t" + str(getDateUTC(chat.date))+ "\t" + str(chat.message))
                    try:
                        if chat.media != None:
                            client.download_media(chat.media, file["image"])
                        if chat.message:
                            new_message = re.sub('0.4|0.5', 'STAKE 1.5', chat.message)
                            if chanel_id_from == 1784783316:
                                new_message = re.sub('S1', 'STAKE 1', new_message)
                                new_message = re.sub('S2', 'STAKE 2', new_message)
                            client.send_message(entity=channel_receive_entity,message=new_message)
                        #almacenar en BD
                        if last_id == 1:
                            last_id = chat.id
                            #si el archivo donde se almacena los id se acaba de crear entonces registrar el ultimo mensaje
                            break                           
                    except Exception as e:
                        writeError(e)
                    break
            #actualizar el nuevo id
            updateLastId(last_id)

        for filename in os.listdir(file["image"]):
            f = os.path.join(file["image"], filename)
            if os.path.isfile(f) and pathlib.Path(filename).suffix == '.jpg':
                client.send_file(channel_receive_entity, f)     
                writeLog(f)             