from pyrogram import Client
app = Client(session_name='pyrogram-assistant',
             bot_token='',
             api_id=1,
             api_hash='b6b154c3707471f5339bd661645ed3d6',
             plugins={'root': 'plugins'})

app.run()
