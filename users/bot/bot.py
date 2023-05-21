import os
import django
from aiogram.utils import executor




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()



from users.bot.create_bot import dp
from users.bot.handlers import register_handlers


async def on_startup(_):
    print('Bot online')

register_handlers(dp)

executor = executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
