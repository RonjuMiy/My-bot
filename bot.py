from aiogram import Bot, Dispatcher, filters
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import os
from aiohttp import web

TOKEN = "8935858251:AAHr47uRXEF3oeafpgGdWrdErPz3geOQYLE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Render Port Check Web Server
async def dummy(request): 
    return web.Response(text='Bot is alive')

async def start_server():
    app = web.Application()
    app.router.add_get('/', dummy)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get('PORT', 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

@dp.message(filters.Command("start"))
async def start(message: Message):
    # নতুন নিয়মে বাটন তৈরি
    btn_my_site = InlineKeyboardButton(
        text="📺 আমার ইউটিউব চ্যানেল", 
        url="https://youtube.com/@premhinjibon?si=-JqYMpv4Hl5UQ0Bs"
    )
    btn_facebook = InlineKeyboardButton(
        text="👤 আমার ফেসবুক প্রোফাইল", 
        url="https://www.facebook.com/share/1DAfoi5npn/"
    )
    
    inline_menu = InlineKeyboardMarkup(inline_keyboard=[[btn_my_site], [btn_facebook]])
    
    await message.answer(
        "আসসালামু আলাইকুম! 🎉 নিচের বাটনগুলোতে ক্লিক করে আমার ইউটিউব চ্যানেল ও ফেসবুক প্রোফাইল চেক করতে পারেন:", 
        reply_markup=inline_menu
    )

async def main():
    await start_server()
    # aiogram v3 তে start_polling এর ভেতর bot পাস করতে হয়
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
