#!/usr/bin/env python3

# (c) https://t.me/TelethonChat/37677

# This Source Code Form is subject to the terms of the GNU

# General Public License, v.3.0. If a copy of the GPL was not distributed with this

# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
try:

    from telethon.sessions import StringSession

    from telethon.sync import TelegramClient

except BaseException:

    print("Telethon Not Found. Installing Now.")

    import os

    os.system("pip3 install telethon")

    from telethon.sessions import StringSession

    from telethon.sync import TelegramClient

ame =""" ______     __    __     ______     ______     ______     ______  
         /\  __ \   /\ "-./  \   /\  ___\   /\  == \   /\  __ \   /\__  _\ 
         \ \  __ \  \ \ \-./\ \  \ \  __\   \ \  __<   \ \ \/\ \  \/_/\ \/ 
          \ \_\ \_\  \ \_\ \ \_\  \ \_____\  \ \_____\  \ \_____\    \ \_\ 
           \/_/\/_/   \/_/  \/_/   \/_____/   \/_____/   \/_____/     \/_/ 

Starting Please wait......

"""

print(ame)

API_ID = int(input("Enter APP ID here: \n"))

API_HASH = input("Enter API HASH here: \n")

client = TelegramClient(StringSession(), API_ID, API_HASH)

with client:

    session_str = client.session.save()

    client.send_message("me", f"`{session_str}`")

    client.send_message(

        "THIS IS YOUR STRING SESSION \nJoin @marshmellowsupport For More Support."

    )

    print("⬆ Please Check Your Telegram Saved Message For Your String Store it safe.")
