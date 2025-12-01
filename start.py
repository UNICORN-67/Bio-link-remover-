from pyrogram import Client

async def send_ready_message(app: Client):
    OWNER_ID = 123456789   # YOUR TG USER ID

    try:
        await app.send_message(OWNER_ID, "🤖 Bot is ready and running successfully!")
        print("DM sent to owner.")
    except Exception as e:
        print(f"Failed to send startup DM: {e}")
