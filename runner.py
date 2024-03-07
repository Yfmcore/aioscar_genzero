from corelib.core import *

from aiogram import *
from aiogram.types import *
from aiogram.exceptions import *
from aiogram.filters import *

# write ur code here

@dp.message(Command(commands=['example']))
async def exampleCommand(msg: Message):
    if mt.isPrivate(msg):
        await msg.reply(f"Hello {msg.from_user.full_name}! This is an example command!")
        
        
if __name__ == '__main__':
    main()