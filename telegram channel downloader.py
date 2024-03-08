from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputPeerEmpty
from tqdm import tqdm


api_id =   # Your API ID as an interger
api_hash = ''  # Your API HASH as an string
starting_message_id =   # Replace with your desired message ID as an integer
title = ''  # Title for channel provide the tittle name of the channel
 

def download_media(group, cl, name, starting_message_id=None):
    print(cl,name)
    messages = cl.iter_messages(group, offset_id=starting_message_id)  # Use iter_messages for performance
    while(starting_message_id>0): #it prevents the auto logout session after 2 hours
        for message in tqdm(messages):
            # Skip messages before the starting_message_id (if provided)
            if starting_message_id and message.id < starting_message_id:
                message.download_media('./' + name + '/') # you can replace the name by string character
                break
        starting_message_id-=1
        print(starting_message_id)
            



with TelegramClient('name', api_id, api_hash) as client:
    result = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=4000,
        hash=0,
    ))

    
    channel = client(GetFullChannelRequest(title))
    channel_id = channel.full_chat.id
    
    # Fetch messages from the channel starting from the specified message (if provided)
    download_media(channel_id, client, title, starting_message_id)
