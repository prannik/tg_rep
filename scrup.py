from telethon import TelegramClient, events, sync


api_id = 16845386
api_hash = 'abd734c6e8a47514f77daeabc55e79e1'
client = TelegramClient('anon', api_id, api_hash)

spisok = ['pam_pidoram', 'me']

@client.on(events.NewMessage(chats=spisok))
async def event_handler(event):
   print(event)
   print('\n')

   print(event.message)



client.start()
client.run_until_disconnected()
