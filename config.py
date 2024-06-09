from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("21946703")
APP_HASH = os.environ.get("e739a8aabffbb28c0f74d1e8fac753a5")
BOT_USERNAME = os.environ.get("Karaz50_bot")
session = os.environ.get("1ApWapzMBu0Bm9T-YxnqKoJBX9zSWlfYsMnf9g0Pq-6Dkvn-SWAo_HtPVpxPHgzSyHCb1kvy_R0KbbCZjxgaA6R__yIm8ommTnE0bArBG22zVysbFIQPcmNyjFg1eafCdhOJpX2xud7nJF7NyhDBu61yyBAqPeK_DPYiKKqHiuvRRyQFLanxrwH2XB0JsliRnq056AKEzNV60d2HmgHY_xQWT6YiLP6imvM85iKL6S92PaYWin0cey00HqUfzFls4FXfhfAT3AYp7U2OtO2B48uCGoMuNVvb6mftSErFknOig3mLhVNlgz3bzz60OhUmQ6eDD-puINjuIxRdwukHm7wrHg6JNeOo=")
SESSION = os.environ.get("1ApWapzMBu0Bm9T-YxnqKoJBX9zSWlfYsMnf9g0Pq-6Dkvn-SWAo_HtPVpxPHgzSyHCb1kvy_R0KbbCZjxgaA6R__yIm8ommTnE0bArBG22zVysbFIQPcmNyjFg1eafCdhOJpX2xud7nJF7NyhDBu61yyBAqPeK_DPYiKKqHiuvRRyQFLanxrwH2XB0JsliRnq056AKEzNV60d2HmgHY_xQWT6YiLP6imvM85iKL6S92PaYWin0cey00HqUfzFls4FXfhfAT3AYp7U2OtO2B48uCGoMuNVvb6mftSErFknOig3mLhVNlgz3bzz60OhUmQ6eDD-puINjuIxRdwukHm7wrHg6JNeOo=")
token = os.environ.get("7292938516:AAF71deWh3ObWtU1tjAPU6Zv6qGHKZqEc7E")
ze = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()