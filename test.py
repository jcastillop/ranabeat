from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest, GetHistoryRequest
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import os

api_id = 22128340
api_hash = '786e2b13cbb94b8209812d1283e1b4db'
chanel = 1675076148 #TITIHENRY LATENIGHT

with TelegramClient('name', api_id, api_hash) as client:
    print('Inicio cliente')
    #Conectarse a entidad especifica 
    # channel_entity=client.get_entity(PeerChannel(chanel))
    # posts = client(GetHistoryRequest(
    #     peer=channel_entity,
    #     limit=100,
    #     offset_date=None,
    #     offset_id=0,
    #     max_id=0,
    #     min_id=0,
    #     add_offset=0,
    #     hash=0))

    #Listar todos los chats
    # for dialog in client.iter_dialogs():
    #     # if dialog.entity.id == 4019284206 or dialog.entity.id == 1784783316:
    #     #     print(dialog.stringify())    
    #     if dialog.is_channel and dialog.name == "Pruebas RanaBeat":
    #         channelId = dialog.entity.id
    #         channelName = dialog.name
    #         print(dialog)
    
    #Enviar mensajes
    channel_receive_entity=client.get_entity(2029273638)
    client.send_message(entity=channel_receive_entity,message="yo soy el mas temeroso ... oni ..chan")
        
    #Enviar imagenes
    # channel_receive_entity=client.get_entity('Pruebas RanaBeat')
    # file = client.upload_file('.\photo_2023-12-11_15-53-36.jpg')
    # client.send_file(channel_receive_entity, file)     

    #mostrar archivos en directorio
    # directory = '.'
 
# iterate over files in
# that directory
    # for filename in os.listdir(directory):
    #     f = os.path.join(directory, filename)
    #     # checking if it is a file
    #     if os.path.isfile(f):
    #         print(f)
    
