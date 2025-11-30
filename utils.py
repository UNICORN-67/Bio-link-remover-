import re

# Regex to detect links inside bio
LINK_REGEX = re.compile(
    r"(https?://|www\.|t\.me/|instagram\.com|facebook\.com|twitter\.com|@[A-Za-z0-9_]{3,})",
    re.IGNORECASE
)

def has_link(bio: str) -> bool:
    return bool(LINK_REGEX.search(bio))
