from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, command
from aiogram.types import FSInputFile
import asyncio

import re

emoji_pattern = re.compile(r"\u2764\ufe0f")

dp = Dispatcher()

@dp.message(command.Command("help"))
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(text="""Your clue is in the \start command... interesting... you're welcomeeee!!!""")

@dp.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(text="""/\_/\  
( o.o )
> <3 < 

~ Hi! I am Agapiii, Welcome! I have a clue for you!
I have 2 puzzle pieces for you.
/gameone for the first puzzle.
/gametwo for the second puzzle.
/help to ask for help in the second puzzle.
/answer to answer the final answer
                     
enter text in keyboard as an answer to both puzzles!
""")

EMOJI_PATTERN = re.compile(
    r"[\U0001F600-\U0001F64F]|"  # Emoticons
    r"[\U0001F300-\U0001F5FF]|"  # Symbols & Pictographs
    r"[\U0001F680-\U0001F6FF]|"  # Transport & Map Symbols
    r"[\U0001F700-\U0001F77F]|"  # Alchemical Symbols
    r"[\U0001F780-\U0001F7FF]|"  # Geometric Shapes Extended
    r"[\U0001F800-\U0001F8FF]|"  # Supplemental Arrows-C
    r"[\U0001F900-\U0001F9FF]|"  # Supplemental Symbols and Pictographs
    r"[\U0001FA00-\U0001FA6F]|"  # Chess Symbols
    r"[\U0001FA70-\U0001FAFF]|"  # Symbols and Pictographs Extended-A
    r"[\U00002702-\U000027B0]|"  # Dingbats
    r"[\U0001F1E0-\U0001F1FF]"   # Flags (iOS)
    r"[\u2700-\u27BF]|"   # Dingbats (includes arrows)
    r"[\u2B05-\u2B07]|"   # Arrows (various directions)
    r"[\u2190-\u21AA]|"   # Arrows (various directions)
    r"[\u2934-\u2935]|"   # Arrows (additional types)
    r"[\u2B06]"           # Upwards Arrow
)

@dp.message(command.Command("help"))
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(text="""Your clue is that the answer is in ASCII art. And the second clue is that the clue for the answer is in the welcome...\n you're welcomeeee!!!""")

@dp.message(command.Command("gameone"))
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(text="""Game1: \nAs a warm up, we will be looking at the camp verse. Complete the missing blanks with emojis of the prayer made by apostle Paul.

'... And I pray that you, being rooted and established in love, 18 may have power, together with all the Lord’s holy people, to grasp how <?> and <?> and <?> and <?> is the <?> of <?> ...'
Extract from Ephesians 17-19
                     
Example: 👍 👎 ❤️ 📏 🐸 🧍‍♂️ 
please use one space between each emoji. thx!!!
answer:""")

@dp.message(command.Command("gametwo"))
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(text="""This is the second game, 
In the beginning, love was written upon the hearts of men,\n a symbol of grace and affection. With the keys bestowed upon thee, 
thou canst fashion this sacred symbol, not with quill nor parchment, but with thy very hands upon the keyboard! How shalt thou craft the shape of love with the tools before thee? 
hint: it is ASCII art instead of an emoji 😉!!! use /help for clue
answer:""")

@dp.message(command.Command("answer"))
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(text="Enter the answer in format <first part of the final answer><second part of the final answer>\n\nExample: if first clue is a, and second clue is b, the answer to key in is\n\n 'ab'   :)")

@dp.message(lambda msg : msg.text == "<3")
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(text="correct! simple, wasn'nt it! lets move on... first part of the answer: Good")
    # await msg.answer_video(video=FSInputFile('feed.mp4'),supports_streaming=True)

@dp.message(lambda msg : msg.text == "What do I need to remove from my life")
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(text="purify yourself with the refiner’s fire")

@dp.message(lambda msg : msg.text == "veryGood")
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(text="correct! simple, wasn'nt it! lets move on... You will not need to use telegram from now on.\n Please wait for the next clue:")
    await msg.answer_video(video=FSInputFile('WhatsApp Video 2024-08-26 at 11.31.47_952f1419.mp4'),supports_streaming=True)

@dp.message(lambda msg : EMOJI_PATTERN.search(msg.text))
async def cmd_start(msg: types.Message) -> None:
    list = msg.text.split(" ")
    print(list)
    if len(list) == 6:
        newlist = ""
        correctlist = [["↔️"],["↕️"],["⬆️"],["⬇️"],["❤️"],["✝️","✝"]]
        naming  = ["1st","2nd","3rd","Forth","5th","6th"]
        corrnum = 0
        for i, element in enumerate(list):
            if element in correctlist[i]:
                newlist += f"The {naming[i]} emoji is ✅!\n"
                corrnum += 1
            else:
                newlist += f"The {naming[i]} emoji is ❌\n"
        if corrnum == 6:
            await msg.answer(text="Correct! The First part of the final answer is: Very")
        else:
            await msg.answer(text=newlist)
    else:
        await msg.answer(text="Please enter 6 emojis with spaces inbetween")

async def main() -> None:
    bot = Bot('') # this is my bot, change the value of the bot token to your own
    await dp.start_polling(bot)

asyncio.run(main())
