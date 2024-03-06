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

async def processResend(chanel_id_from, chanel_type, chanel_id_to):

    file = appVars["file"]
    last_id = getLastId(chanel_id_from)
    try:     
        async with TelegramClient('name', params.api_id, params.api_hash) as client:
            entity = PeerChat(chanel_id_from)
            if chanel_type:
                entity = PeerChannel(chanel_id_from)
            channel_entity= await client.get_entity(entity)
            channel_receive_entity= await client.get_entity(chanel_id_to)
            posts = await client(GetHistoryRequest(
                peer=channel_entity,
                limit=5,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0))
            print( "Canal: " + str(chanel_id_from) + " - ID registrado en TXT: " + str(last_id)+ " ultimo chat encontrado " + str(posts.messages[0].id) )

            if last_id != posts.messages[0].id:
                new_last_id = int(posts.messages[0].id)
                updateLastId(new_last_id)
                x = range(new_last_id - 4, new_last_id + 1)
                for n in x:
                    if( int(n) > 0 and int(n) > last_id):
                        chat = await client.get_messages(channel_entity, ids=int(n))
                        writeLog(str(chat.id) + "\t" + str(getDateUTC(chat.date))+ "\t" + str(chat.message))
                        if chat.media != None:
                            await client.download_media(chat.media, file["image"])
                        if chat.message:
                            new_message = re.sub('0.4|0.5', 'STAKE 1.5', chat.message)
                            new_message = re.sub('S1', 'STAKE 1', new_message)
                            new_message = re.sub('S2', 'STAKE 2', new_message)
                            await client.send_message(entity=channel_receive_entity,message=new_message)

            # while last_id != posts.messages[0].id:
            #     print( "Chat nuevo encontrado con id: " + str(posts.messages[0].id))
            #     last_id += 1
            #     for chat in posts.messages:
            #         print( "Evaluando el id: " + str(last_id))
            #         if (chat.id == last_id) or (last_id==1):
            #             writeLog(str(chat.id) + "\t" + str(getDateUTC(chat.date))+ "\t" + str(chat.message))

            #             if chat.media != None:
            #                 client.download_media(chat.media, file["image"])
            #             if chat.message:
            #                 new_message = re.sub('0.4|0.5', 'STAKE 1.5', chat.message)
            #                 new_message = re.sub('S1', 'STAKE 1', new_message)
            #                 new_message = re.sub('S2', 'STAKE 2', new_message)
            #                 client.send_message(entity=channel_receive_entity,message=new_message)
            #             #almacenar en BD
            #             if last_id == 1:
            #                 last_id = chat.id
            #                 #si el archivo donde se almacena los id se acaba de crear entonces registrar el ultimo mensaje
            #                 break
            #             break
            #     #actualizar el nuevo id
            #     updateLastId(last_id)

            for filename in os.listdir(file["image"]):
                f = os.path.join(file["image"], filename)
                if os.path.isfile(f) and pathlib.Path(filename).suffix == '.jpg':
                    await client.send_file(channel_receive_entity, f)     
                    writeLog(f)    
    except Exception as e:
        writeError(str(chanel_id_from))
        writeError(e)