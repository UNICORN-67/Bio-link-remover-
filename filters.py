import re

BIO_PATTERNS = [
    # Bio / Social / Promo links
    r"bio\.link",
    r"taplink\.cc",
    r"beacons\.ai",
    r"linktree\.com",
    r"linktr\.ee",
    r"onlyfans\.com",
    r"fansly\.com",
    r"fancentro\.com",
    r"carrd\.co",
    r"about\.me",
    r"my\.bio",
    r"instagr\.am",
    r"instagram\.com",

    # Short URLs
    r"bit\.ly\/.+",
    r"tinyurl\.com\/.+",
    r"t\.co\/.+",
    r"mega\.nz\/.+",
    r"drive\.google\.com\/.+",

    # Telegram links
    r"t\.me\/\w+",
    r"https:\/\/t\.me\/\w+",

    # Username tagging spam
    r"@\w{4,}",                # @abcd (min 4)
    r"(join|follow|dm|contact)\s*@\w+",

    # Promo keywords
    r"follow\s+me",
    r"dm\s+me",
    r"promo\s+code",
    r"check\s+my",
    r"my\s+link",
    r"profile\s+link",
]

COMPILED_PATTERNS = [re.compile(p, re.IGNORECASE) for p in BIO_PATTERNS]
