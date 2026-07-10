from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

TOKEN = "8935858251:AAHr47uRXEF3oeafpgGdWrdErPz3geOQYLE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(commands=['start'])
async def start(message: Message):
    inline_menu = InlineKeyboardMarkup(row_width=1)
    
    # আপনার দেওয়া ইউটিউব লিংক (ফিক্সড)
    btn_my_site = InlineKeyboardButton(
        text="📺 আমার ইউটিউব চ্যানেল", 
        url="https://youtube.com/@premhinjibon?si=-JqYMpv4Hl5UQ0Bs"
    )
    
    # आपका দেওয়া ফেসবুক লিংক (ফিক্সড)
    btn_facebook = InlineKeyboardButton(
        text="👤 আমার ফেসবুক প্রোফাইল", 
        url="https://www.facebook.com/share/1DAfoi5npn/"
    )
    
    # বাটনগুলো মেনুতে যোগ করা হলো
    inline_menu.add(btn_my_site, btn_facebook)
    
    await message.answer(
        "আসসালামু আলাইকুম! 🎉 নিচের বাটনগুলোতে ক্লিক করে আমার ইউটিউব চ্যানেল ও ফেসবুক প্রোফাইল চেক করতে পারেন:", 
        reply_markup=inline_menu
    )

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.get_event_loop().create_task(start_server())
    asyncio.run(main())


import os
import asyncio
from aiohttp import web
async def dummy(request): return web.Response(text='Bot is alive')
async def start_server():
    app = web.Application()
    app.router.add_get('/', dummy)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get('PORT', 8080)))
    await site.start()
