from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.all_kb import *
from db_handler.worker import *

p1, p2, p3 = [9, 11, 13], [0, 50, 100], [2500, 5000, 10000]
a1 = ['8-9 класс', '10-11 класс', 'Студент']
a2 = ['Плохо, не думаю, что сдам', 'Не знаю, сдам или нет', 'Уверен, что сдам, просто повторить']
aa2 = ['Не готов', 'Частично готов', 'Готов']
a3 = ['Короткой (~2500 символов)', 'Средней (~5000 символов)', 'Длинной (~10000 символов)']



start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message): # проверка настроек, рабаота с sqlite
    a = data_tester(user_telegram_id=message.from_user.id)
    uncommited = 0
    #print(*a)
    if a[1] == 1:
        uncommit_error(message.from_user.id)
        uncommited = 1
    if a[0] != 3 or uncommited == 1:
        start_user(message.from_user.id)
        await message.answer('Привет!\nЭтот бот позволяет улучшить или повторить знания, необходимые для сдачи необходимых экзаменов.\n'
                            'Чтобы лучше подобрать материал, необходимо ответить на несколько простых вопросов.\nВ каком классе ты учишься?', reply_markup=oobe_part_2())
    else:
        await message.answer('Бот был перезапущен')


@start_router.message(F.text.in_({'8-9 класс', '10-11 класс', 'Студент'}))
async def oobe1(message: Message):
    k1 = p1[a1.index(message.text)]
    k2 = message.from_user.id
    a = data_tester(user_telegram_id=message.from_user.id)
    if a[0] == 0:
        try:
            OOBE_Part1(k1, k2)
            await message.answer('Насколько хорошо, по твоему мнению, ты подготовлен?', reply_markup=oobe_part_3())
        except:
            commit_error(k2)
            await message.answer('Произошла ошибка во время первоначальной настройки. Перезапустите бота, если это не помогло, свяжитесь с автором:\n'
                                 'Почта: nik.sanin.06@mail.ru\nTelegram: @nikitasanin2006', reply_markup=delete_keyboard())
            pass
    if a[1] == 1:
        await message.answer("Из-за ранее возникшей ошибки работа бота невозможна.\nПопробуйте перезапустить бота командой /start, если это не поможет, свяжитесь с автором:\n"
        "Почта: nik.sanin.06@mail.ru\nTelegram: @nikitasanin2006")


@start_router.message(F.text.in_({'Плохо, не думаю, что сдам', 'Не знаю, сдам или нет', 'Уверен, что сдам, просто повторить'}))
async def oobe2(message: Message):
    k1 = p2[a2.index(message.text)]
    k2 = message.from_user.id
    a = data_tester(user_telegram_id=message.from_user.id)
    if a[0] == 1:
        try:
            OOBE_Part2(k1, k2)
            await message.answer('Также в боте есть возможность выделять главное из всего материала - делать суммаризацию.\nНасколько '
                                 'длинной она должна быть?', reply_markup=oobe_part_4())
        except:
            commit_error(k2)
            await message.answer(
                'Произошла ошибка во время первоначальной настройки. Перезапустите бота, если это не помогло, свяжитесь с автором:\n'
                'Почта: nik.sanin.06@mail.ru\nTelegram: @nikitasanin2006', reply_markup=delete_keyboard())
            pass
    if a[1] == 1:
        await message.answer("Из-за ранее возникшей ошибки работа бота невозможна.\nПопробуйте перезапустить бота командой /start, если это не поможет, свяжитесь с автором:\n"
        "Почта: nik.sanin.06@mail.ru\nTelegram: @nikitasanin2006")

@start_router.message(F.text.in_({'Короткой (~2500 символов)', 'Средней (~5000 символов)', 'Длинной (~10000 символов)'}))
async def oobe3(message: Message):
    k1 = p3[a3.index(message.text)]
    k2 = message.from_user.id
    a = data_tester(user_telegram_id=message.from_user.id)
    if a[0] == 2:
        try:
            OOBE_Part3(k1, k2)
            await message.answer("Готово! Теперь можно пользоваться! :D\n\nПросто введи в чат тему для изучения, и бот предоставит необходимый материал.\n"
                                                       "Например: механические колебания\n\n(ГОТОВА ТОЛЬКО ПЕРВОНАЧАЛЬНАЯ НАСТРОЙКА)", reply_markup=main_kb(message.from_user.id))
        except:
            commit_error(k2)
            await message.answer('Произошла ошибка во время первоначальной настройки. Перезапустите бота, если это не помогло, свяжитесь с автором:\n'
                                 'Почта: nik.sanin.06@mail.ru\nTelegram: @nikitasanin2006', reply_markup=delete_keyboard())
            pass
    if a[1] == 1:
        await message.answer("Из-за ранее возникшей ошибки работа бота невозможна.\nПопробуйте перезапустить бота командой /start, если это не поможет, свяжитесь с автором:\n"
        "Почта: nik.sanin.06@mail.ru\nTelegram: @nikitasanin2006")



@start_router.message(F.text == 'Контакты')
async def cmd_start_3(message: Message):
    await message.answer("Вы можете связаться с автором:\nПочта: nik.sanin.06@mail.ru\nTelegram: @nikitasanin2006\n"
                                               "Если у вас возникнут какие-либо проблемы, перед вашим обращением сначала перезапустите бота, написав /start.\n\n"
                         "Есть какие-либо предложения насчёт бота?\nСвяжитесь с автором, возможно, именно ваша идея будет "
                         "реализована.", reply_markup=main_kb(message.from_user.id))


@start_router.message(F.text == 'Настройки')
async def setting(message: Message):
    get = get_settings(message.from_user.id)
    if None not in get:
        stri = 'Текущие настройки:\nКласс: ' + a1[p1.index(get[0])] + '\nСамооценка: ' + aa2[p2.index(get[1])] + '\nДлина суммаризации: ~' + str(get[2]) + ' символов'
        await message.answer(stri, reply_markup=main_kb(message.from_user.id))

@start_router.message(F.text == 'Сбросить настройки')
async def setting(message: Message):
    get = get_settings(message.from_user.id)
    a = data_tester(user_telegram_id=message.from_user.id)
    if a[1] == 1:
        await message.answer("Чтобы устранить возникшую ошибку, необходим перезапуск бота.\nНастройки будут автоматически сброшены.")
    elif None not in get:
        delete_user(message.from_user.id)
        await message.answer("Настройки были успешно сброшены. Перезапустите бота для продолжения работы.", reply_markup=delete_keyboard())



@start_router.message(F.text)
async def message(message: Message):
    a = data_tester(user_telegram_id=message.from_user.id)
    if a[0] == 3:
        await message.answer("Готова только первоначальная настройка", reply_markup=main_kb(message.from_user.id))





