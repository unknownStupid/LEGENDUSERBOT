import time

from telethon import version
from userbot import ALIVE_NAME, StartTime, LEGENDversion
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "ℓєgєи∂ϐοτ"
LEGEND_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "ℓєgєи∂ Choice ℓєgєи∂ϐοτ"
CUSTOM_MY_GROUP =Config.MY_GROUP or "@Legend_Userbot"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if  LEGEND_IMG:
        LEGEND_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        
        LEGEND_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        LEGEND_caption += f"     💫 𝕭𝖔𝖙 𝕾𝖙𝖆𝖙𝖚𝖘 💫\n"
        LEGEND_caption += f"•⚜️• Owner      : {mention}\n\n"
        LEGEND_caption += f"•⚡• Bot  : {LEGENDversion}\n"
        LEGEND_caption += f"•⚡• Telethon  : `{version.__version__}`\n"
        LEGEND_caption += f"•⚡• Uptime      : `{uptime}`\n"
        LEGEND_caption += f"•⚡• channel       : [𝕲𝖗𝖔𝖚𝖕](t.me/MythicStickers)\n"
        LEGEND_caption += f"•⚡• Mγ Gяουρ : {CUSTOM_MY_GROUP}\n"   

        await alive.client.send_file(
            alive.chat_id, LEGEND_IMG, caption=LEGEND_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         𝕭𝖔𝖙 𝕾𝖙𝖆𝖙𝖚𝖘\n"
            f"•⚡• 𝕿єℓєτнοи    : `{version.__version__}`\n"
            f"🇮🇳 ℓєgєи∂ϐοτ  : `{LEGENDversion}`\n"
            f"🇮🇳 υρτιмє        : `{uptime}`\n"
            f"🔱 ɱαรƭεɾ        : {mention}\n"
            f"🔱 σωɳεɾ         : [ℓєgєи∂](t.me/MythicStickers)\n"
        )

CmdHelp("ɓσƭรƭαƭµร").add_command(
    'bot', None, 'υѕє αи∂ ѕєє'
).add()
