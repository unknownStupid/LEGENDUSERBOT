import asyncio
from . import *
@bot.on(admin_cmd(pattern="happybirthday"))
async def birthday(ult):
	await asyncio.sleep(1)
	await ult.edit("""
▃▃▃▃▃▃▃▃▃▃▃
┊ ┊ ┊ ┊ ┊ ┊
┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩
┊ ┊ ┊ ✫
┊ ┊ ✧🎂🍰🍫🍭
┊ ┊ ✯
┊ . ˚ ˚✩
........♥️♥️..........♥️♥️_
.....♥️........♥️..♥️........♥️_
...♥️.............♥️............♥️
......♥️.....Happy.......♥️
...........♥️..............♥️
................♥️.....♥️
......................♥️
...............♥️........♥️
..........♥️...............♥️
.......♥️..Birthday....♥️_
.....♥️..........♥️...........♥️
.....♥️.......♥️_♥️.....♥️
.........♥️♥️........♥️♥️.....
.............................................
..... (¯`v´¯)♥️
.......•.¸.•´STAY BLESSED
....¸.•´      LOVE&FUN
... (   YOU DESERVE
☻/ THEM A LOT
/▌✿🌷✿
/ \     \|/\n▃▃▃▃▃▃▃▃▃▃▃
""")
CmdHelp("goodnight").add_command(
'gm', None, 'Use and See'
).add()
