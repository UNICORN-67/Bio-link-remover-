from pyrogram import Client, filters, idle
from start import send_ready_message
from bioremover import check_and_delete_biolink

# ------------------------------
# CONFIG
# ------------------------------
API_ID = 16841147                     # CHANGE THIS
API_HASH = "724367ca3534a7e37594fcf3512dc8ad"    # CHANGE THIS
BOT_TOKEN = "8527857229:AAGZhx7hO4i85PJaXz8x4GHjFXFvQiUuZmA"  # CHANGE THIS
OWNER_ID = 7621384600               # CHANGE THIS (YOUR TELEGRAM ID)


# ------------------------------
# CLIENT
# ------------------------------
app = Client(
    "BioLinkRemoverBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


# ------------------------------
# /start for DM
# ------------------------------
@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    await message.reply_text(
        "👋 **Hello! I'm the Bio-Link Remover Bot!**\n\n"
        "➤ Add me to a group as admin\n"
        "➤ I will automatically delete bio-links, @ mentions spam, "
        "and promo links.\n"
    )


# ------------------------------
# AUTO BIO-LINK CHECKER
# ------------------------------
@app.on_message(filters.group, group=1)
async def bio_check_handler(client, message):
    await check_and_delete_biolink(client, message)


# ------------------------------
# STARTUP DM TO OWNER
# ------------------------------
@app.on_message(filters.private & filters.regex("^__startup__internal__$"))
async def internal_startup(client, message):
    await send_ready_message(app)


# ------------------------------
# APP STARTER
# ------------------------------
async def startup_dm():
    try:
        await app.send_message(OWNER_ID, "__startup__internal__")
    except:
        print("Owner DM startup message failed.")


app.start()
app.loop.run_until_complete(startup_dm())
print("🚀 Bot is running...")
idle()
app.stop()
