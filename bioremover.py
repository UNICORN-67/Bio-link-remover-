from filters import COMPILED_PATTERNS
from pyrogram.errors import MessageDeleteForbidden

async def check_and_delete_biolink(client, message):

    if not message.text:
        return

    text = message.text.lower()

    for pattern in COMPILED_PATTERNS:
        if pattern.search(text):

            print(f"Detected pattern: {pattern.pattern}")

            try:
                await message.delete()
                print("Deleted a bio-link or @promotion message.")
            except MessageDeleteForbidden:
                print("Bot missing delete permission in this group.")
            except Exception as e:
                print(f"Error deleting: {e}")

            return
