from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
from config import API_ID, API_HASH, BOT_TOKEN
from utils import has_link

app = Client(
    "bio_link_remover",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_chat_member_updated()
async def bio_check(_, update: ChatMemberUpdated):
    if not update.new_chat_member:
        return

    user = update.new_chat_member.user

    # Ignore bots
    if user.is_bot:
        return

    bio = user.bio or ""

    # Check for links
    if has_link(bio):
        try:
            await update.chat.kick_member(user.id)
            await update.chat.unban_member(user.id)

            await app.send_message(
                update.chat.id,
                f"🚫 **Bio link detected!**\n\n"
                f"User: [{user.first_name}](tg://user?id={user.id})\n"
                f"Action: **Kicked** (remove bio link to join again)"
            )
        except Exception as e:
            await app.send_message(update.chat.id, f"Error: `{e}`")


print("Bot started...")
app.run()
