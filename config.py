# Telegram API credentials (load from .env in main.py)
API_ID = None
API_HASH = None

#Changed from Random to AI as the new behaviour
GEMINI_API_KEY = None # <<< IMPORTANT: Get this from Google AI Studio
MODE = "AI"
# ---------------------------

# Channels you want to monitor
CHANNELS = ["tiktokleadsgen",
            "stockverified",
            "onemindset",
            "Psycho_Motivations",
            "QuotesCafe1",
            "crypto_business_quotes",
            "positivity",
            "love_quotes",
            "Quotes_Facts_English_Motivation",
            "yourshopefully",
            "general_thoughts",
            "Audiobooks_collection",
            "Books_readers_hub",
            "profile_pictures_TM",
            "premium_ebooks",
            "offical_dark_feelings",
            "ThinkPositivePower",
            "TonyRobbinson",
            "sosavage_memes",
            "success_books_2",
            "Profile_PicturesHD",
            "B_Flew",
            "DGPIndia",
            "Moonlight_thoughtss",
            "quotemaster",
            "Musics_and_Quotes",
            "business_talkk",
            "TheMasculineKing",
            "stoicchads",
            "AttractHer",
            "fastlifegang",
            "eduphilespace",
            "books",
            "quoteshubb",
            "TheMenBuilder",
            "TheTrlbe",
            "overmind011",
            "CMMWarriors",
            "MAGNETICDEVILS",
            "Powerandwealth",
            "Brighten_Up_Your_Mind",
            "Leaders_Junction",
            "newmentalities",
            "Successpictures",
            "MindPsychologyy",
            "BizTip101",
            "DurablemanInstitute",
            "escape_ism",
            "GreaseTheWheelzz",
            "MasculineClub",
            "bussiness_tip",
            "book_lists",
            "self_growth_book",
            "MVDailyTips",
            "gsandgirls",
            "Crypto_News_Ke",
            "bookreviewizB",
            "womanthinkk",
            "motivationacti",
            "thehouseofpower",
            "MasculineMindz",
            "MajestyMasculinee",
            "TheEdenApple",
            "Inspire_motivate_freedom",
            -1002404659940 #Practicals channel
            ]

# Behaviour controls
DELAY_RANGE = (15, 60)
SKIP_PROBABILITY = 0.3
LOG_ONLY = False  # For posting on comments, I'll change to True if I want logs print only
# Reply queue settings: how long to keep trying to find the discussion message (seconds)
# Increased to 300s to allow the discussion message to appear and conversion to threaded reply
REPLY_QUEUE_MAX_WAIT = 300
# Poll interval for queued jobs (seconds)
REPLY_QUEUE_POLL_INTERVAL = 3
# Local cooldown per linked discussion to avoid flood limits (seconds)
COOLDOWN = 300
# How many recent messages to scan when searching for the discussion message
REPLY_QUEUE_SEARCH_LIMIT = 1000
# If True, allow reply jobs to be queued even when the server requests a wait longer
# than REPLY_QUEUE_MAX_WAIT. Use with caution — this can cause jobs to sit for long periods.
REPLY_QUEUE_ALLOW_LONG_WAIT = False
# When allowing long waits, add this slack (seconds) after the required wait before giving up
REPLY_QUEUE_LONG_WAIT_SLACK = 60
# When True, dump a compact debug view of recent messages for a discussion when mapping fails
DEBUG_DUMP_RECENT = True