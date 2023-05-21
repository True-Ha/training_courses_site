from aiogram import Dispatcher, types
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.message import ContentType

from users.services import create_user, create_payment_info
from .create_bot import bot, dp
from .dataconfig import PAYMENTS_TOKEN


class RegisterFSM(StatesGroup):
    username = State()
    email = State()
    password = State()
    r_password = State()


PRICE = types.LabeledPrice(label="Подписка на 1 месяц", amount=5000*100) #в копеейках
password = None

async def start_registration(message: Message):
    await RegisterFSM.username.set()
    await message.reply('Укажите свой username')


async def set_username(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await RegisterFSM.next()
    await message.reply('Укажите свою почту')


async def set_email(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await RegisterFSM.next()
    await message.reply('Укажите пароль')

async def set_password(message: Message, state: FSMContext):
    global password
    async with state.proxy() as data:
        data['password'] = message.text
        password = data['password']
    await RegisterFSM.next()
    await message.reply('Повторите пароль')

async def r_password_invalid(message: Message):
    await message.reply('Не правильный пароль')

async def check_password(message: Message, state: FSMContext):
    async with state.proxy() as data:
        created, user = await create_user(
            t_name=message.from_user.first_name,
            t_username=message.from_user.username,
            t_user_id=message.from_user.id,
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
    if created:
        await message.reply('Учетная запись успешно создана')
    else:
        await message.reply('Пользователь с таким username уже занят')
    await state.finish()


async def start(message: Message):
    await message.answer('Команды: \n/buy_course\n/reg')


async def buy_course(message: Message):
    if PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Test payment!!!")

    await bot.send_invoice(message.chat.id,
                           title="Buy course",
                           description="Body training course",
                           provider_token=PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://i.pinimg.com/600x315/0f/e0/05/0fe005679f54e54358f480c0ffe7aa34.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subsription",
                           payload="test-invoice-payload"
                           )


#pre checkout (must be answered in 10 seconds)
@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

#successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def success_payment(message: Message):
    print("SUCCESSFUL PAYMENT")
    payment_info = message.successful_payment.to_python()
    await bot.send_message(message.chat.id,
                           f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошёл успешно")
###########
    await (create_payment_info(message.from_user.id, message.from_user.first_name, message.from_user.username, payment_info))



###########
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_registration, commands='reg', state=None)
    dp.register_message_handler(set_username, state=RegisterFSM.username)
    dp.register_message_handler(set_email, state=RegisterFSM.email)
    dp.register_message_handler(set_password, state=RegisterFSM.password)
    dp.register_message_handler(r_password_invalid, lambda message: message.text != password, state=RegisterFSM.r_password)
    dp.register_message_handler(check_password, lambda message: message.text == password, state=RegisterFSM.r_password)
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(buy_course, commands='buy_course')
    dp.register_message_handler(pre_checkout_query, lambda query: True)
    dp.register_message_handler(success_payment, content_types=ContentType.SUCCESSFUL_PAYMENT)