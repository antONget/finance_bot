import calendar
import datetime
from unicodedata import category
from inspect import currentframe, getframeinfo

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

import module

def get_main_keyboard():
    frameinfo = getframeinfo(currentframe())
    """
    Вывод стартовой клавиатуры для приветственного сообщения
    :return: Стартовая клавиатура с переходом к меню
    """
    print('keyboards.py->get_main_keyboard', f'#{frameinfo.lineno}', 'добавление кнопки "Главное меню"')
    main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    main_menu = InlineKeyboardButton('🏠 Главное меню')
    main_keyboard.add(main_menu)

    return main_keyboard

def get_start_keyboard() -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод стартовой клавиатуры для приветственного сообщения
    :return: Стартовая клавиатура с переходом к меню
    """
    print('keyboards.py->get_start_keyboard', f'#{frameinfo.lineno}','клавиатура при нажатии кнопки /start')
    start_keyboard = InlineKeyboardMarkup()
    menu = InlineKeyboardButton('📋 Меню', callback_data='menu')
    setting = InlineKeyboardButton('⚙️ Настройки', callback_data='setting')
    start_keyboard.add(menu, setting)

    return start_keyboard


def get_menu_keyboard() -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клаиватуры меню
    :return: Клавиатура меню
    """
    print('keyboards.py->get_menu_keyboard', f'#{frameinfo.lineno}', 'клавиатура при нажатии кнопки /menu')
    menu_keyboard = InlineKeyboardMarkup(row_width=1)
    position = InlineKeyboardButton('➕ Добавить', callback_data='add')
    statistics = InlineKeyboardButton('📈 Аналитика', callback_data='statistics')
    menu_keyboard.add(position, statistics)

    return menu_keyboard

def get_setting_keyboard() -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клаиватуры меню
    :return: Клавиатура меню
    """
    print('keyboards.py->get_menu_setting', f'#{frameinfo.lineno}', 'клавиатура при нажатии кнопки Настройки')
    setting_keyboard = InlineKeyboardMarkup()
    categorys = InlineKeyboardButton('Категории', callback_data='categorys')
    limits = InlineKeyboardButton('Лимиты', callback_data='limits')
    setting_keyboard.add(categorys, limits)

    return setting_keyboard

def get_edit_category() -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    клавиатура при нажатии кнопки Настройки/
    :return: Клавиатура меню
    """
    print('keyboards.py->get_edit_category', f'#{frameinfo.lineno}', 'клавиатура при нажатии кнопки Настройки/')
    setting_keyboard = InlineKeyboardMarkup()
    del_cat = InlineKeyboardButton('Удалить', callback_data='del_cat')
    add_cat = InlineKeyboardButton('Добавить', callback_data='add_cat')
    setting_keyboard.add(del_cat, add_cat)
    # print('keyboard create')
    return setting_keyboard

def get_edit_limit() -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клаиватуры правки лимитов
    :return: Клавиатура меню
    """
    print('keyboards.py->get_edit_limit', f'#{frameinfo.lineno}', 'клавиатура при для правки лимита по категории')
    limit_edit_keyboard = InlineKeyboardMarkup()
    edit_limit = InlineKeyboardButton('Изменить', callback_data='edit_limit')
    pass_limit = InlineKeyboardButton('Пропустить', callback_data='pass_limit')
    limit_edit_keyboard.add(edit_limit, pass_limit)

    return limit_edit_keyboard

def get_add_bonus() -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Диалог для указания баллов
    :return: Клавиатура меню
    """
    print('keyboards.py->get_add_bonus', f'#{frameinfo.lineno}', 'Диалог для указания баллов')
    add_bonus_keyboard = InlineKeyboardMarkup()
    pass_bonus = InlineKeyboardButton('Пропустить', callback_data='pass_bonus')
    add_bonus_keyboard.add(pass_bonus)

    return add_bonus_keyboard

def get_plus_minus_keyboard() -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клаиватуры выбора типа позиции
    :return: Клавиатура для выбора дохода или расхода
    """
    print('keyboards.py->get_plus_minus_keyboard', f'#{frameinfo.lineno}', 'клаиватура при нажатии кнопки Добавить')
    plus_minus_keyboard = InlineKeyboardMarkup(row_width=2)
    plus_button = InlineKeyboardButton("➕ Доход", callback_data='income')
    minus_button = InlineKeyboardButton("➖ Расход", callback_data='expense')
    back = InlineKeyboardButton('⬅ Назад', callback_data='menu')
    plus_minus_keyboard.add(plus_button, minus_button, back)

    return plus_minus_keyboard

def get_plus_minus_limit_keyboard() -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клаиватуры выбора типа позиции
    :return: Клавиатура для выбора дохода или расхода
    """
    print('keyboards.py->get_plus_minus_limit_keyboard', f'#{frameinfo.lineno}', 'клаиватура при нажатии кнопки изменить Лимит')
    plus_minus_limit_keyboard = InlineKeyboardMarkup(row_width=2)
    plus_button = InlineKeyboardButton("➕ Доход", callback_data='income_limit_update')
    minus_button = InlineKeyboardButton("➖ Расход", callback_data='expense_limit_update')
    back = InlineKeyboardButton('⬅ Назад', callback_data='menu')
    plus_minus_limit_keyboard.add(plus_button, minus_button, back)

    return plus_minus_limit_keyboard

def get_plus_minus_update_category_keyboard() -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    клавиатура при нажатии клавижи Настройки
    :return: Клавиатура для выбора дохода или расхода
    """
    print('keyboards.py->get_plus_minus_update_category_keyboard', f'#{frameinfo.lineno}', 'клавиатура при нажатии клавижи Настройки')
    plus_minus_limit_keyboard = InlineKeyboardMarkup(row_width=2)
    plus_button = InlineKeyboardButton("➕ Доход", callback_data='income_update')
    minus_button = InlineKeyboardButton("➖ Расход", callback_data='expense_update')
    back = InlineKeyboardButton('⬅ Назад', callback_data='start')
    plus_minus_limit_keyboard.add(plus_button, minus_button, back)

    return plus_minus_limit_keyboard    

def get_categories_keyboard(position_type: str) -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клаиватуры выбора категории для внесения позиции
    :return: Клавиатура с категориями
    """
    print('keyboards.py->get_categories_keyboard', f'#{frameinfo.lineno}', 'Вывод клаиватуры выбора категории')
    categories_keyboard = InlineKeyboardMarkup(row_width=1)
    categories = module.get_categories(position_type)
    for id in range(len(categories)):
        category = InlineKeyboardButton(str(categories[id][0]), callback_data=str(id))
        categories_keyboard.add(category)

    return categories_keyboard

def get_delcategories_keyboard(position_type: str) -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клаиватуры выбора категории для удаления
    :return: Клавиатура с категориями
    """
    print('keyboards.py->get_delcategories_keyboard', f'#{frameinfo.lineno}', 'Вывод клаиватуры выбора категории удаления категории')
    del_categories_keyboard = InlineKeyboardMarkup(row_width=1)
    categories = module.get_categories(position_type)
    for id in range(len(categories)):
        category = InlineKeyboardButton(str(categories[id][0]), callback_data='del_categor_'+str(id))
        del_categories_keyboard.add(category)
    # print('finish->get_delcategories_keyboard')
    return del_categories_keyboard

def get_updatelimit_keyboard(position_type: str) -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клаиватуры выбора категории для изменения лимита
    :return: Клавиатура с категориями
    """
    print('keyboards.py->get_updatelimit_keyboard', f'#{frameinfo.lineno}', 'Вывод клаиватуры выбора категории изменения лимита')
    del_categories_keyboard = InlineKeyboardMarkup(row_width=1)
    categories = module.get_categories(position_type)
    for id in range(len(categories)):
        category = InlineKeyboardButton(str(categories[id][0]), callback_data= str(id) + f'_update_limit_cat')
        del_categories_keyboard.add(category)
    # print('finish->get_delcategories_keyboard')
    return del_categories_keyboard


def get_date_keyboard() -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клаиватуры для выбора даты
    :return: Клавиатура выбора даты
    """
    print('keyboards.py->get_date_keyboard', f'#{frameinfo.lineno}', 'Вывод клаиватуры "сегодня-вчера-другой день" ')
    date_keyboard = InlineKeyboardMarkup(row_width=3)
    today = InlineKeyboardButton("Сегодня", callback_data='today')
    yesterday = InlineKeyboardButton("Вчера", callback_data='yesterday')
    other = InlineKeyboardButton('Другой день', callback_data='other')
    date_keyboard.add(today, yesterday, other)

    return date_keyboard


def get_confirm_keyboard() -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клаиватуры подтверждения информации о позиции
    :return: Клавиатура для подтверждения
    """
    print('keyboards.py->get_confirm_keyboard', f'#{frameinfo.lineno}', 'Вывод клаиватуры подтверждения информации о позиции')
    confirm_keyboard = InlineKeyboardMarkup(row_width=2)
    yes = InlineKeyboardButton("Да", callback_data='confirm')
    no = InlineKeyboardButton("Отмена", callback_data='cancel')
    confirm_keyboard.add(yes, no)

    return confirm_keyboard


def get_calendar_keyboard(year=None, month=None) -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клаиватуры с календарём для выбора даты
    :return: Клавиатура календаря
    """
    print('keyboards.py->get_calendar_keyboard', f'#{frameinfo.lineno}', 'Вывод клаиватуры с календарём для выбора даты')
    now = datetime.datetime.now()
    if year is None:
        year = now.year
    if month is None:
        month = now.month
    keyboard = []
    row1 = [InlineKeyboardButton(module.month_name(month) + " " + str(year),
                                 callback_data=";".join(['ignore', str(0), str(month), str(year)]))]
    keyboard.append(row1)
    row2 = []
    for day in ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]:
        row2.append(InlineKeyboardButton(day,
                                         callback_data=";".join(['ignore', str(day), str(month), str(year)])))
    keyboard.append(row2)

    my_calendar = calendar.monthcalendar(year, month)
    for week in my_calendar:
        row3 = []
        for day in week:
            if day == 0:
                row3.append(InlineKeyboardButton(" ",
                                                     callback_data=";".join(
                                                         ['ignore', str(day), str(month), str(year)])))
            else:
                row3.append(InlineKeyboardButton(str(day),
                                                     callback_data=";".join(['day', str(day), str(month), str(year)])))
        keyboard.append(row3)

    row4 = [InlineKeyboardButton("<",
                                 callback_data=";".join(['prev_month', str(1), str(month), str(year)])),
            InlineKeyboardButton(" ",
                                 callback_data=";".join(['ignore', str(0), str(month), str(year)])),
            InlineKeyboardButton(">",
                                 callback_data=";".join(['next_month', str(1), str(month), str(year)]))]
    keyboard.append(row4)

    return InlineKeyboardMarkup(keyboard)


def get_statistics_keyboard() -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клаиватуры меню статистики
    :return: Клавиатура меню статистики
    """
    print('keyboards.py->get_statistics_keyboard', f'#{frameinfo.lineno}', 'Вывод клаиватуры меню статистики')
    statistics_keyboard = InlineKeyboardMarkup(row_width=2)
    default = InlineKeyboardButton('Статистика доходов', callback_data='income_statistics')
    categories = InlineKeyboardButton('Статистика расходов', callback_data='expense_statistics')
    back = InlineKeyboardButton('⬅ Назад️', callback_data='menu')
    statistics_keyboard.add(default, categories, back)

    return statistics_keyboard


def get_statistics_keyboard_types() -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клаиватуры статистики с типами
    :return: Клавиатура меню статистики
    """
    print('keyboards.py->get_statistics_keyboard_types', f'#{frameinfo.lineno}', 'Вывод клаиватуры статистики с типами')
    statistics_keyboard = InlineKeyboardMarkup(row_width=2)
    default = InlineKeyboardButton('Общая статистика', callback_data='default_statistics')
    categories = InlineKeyboardButton('По категориям', callback_data='categories_statistics')
    back = InlineKeyboardButton('⬅ Назад️', callback_data='statistics')
    statistics_keyboard.add(default, categories, back)

    return statistics_keyboard


def get_statistics_period_keyboard(positions_type: str) -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Вывод клавиатуры периода показа статистики
    :param positions_type: Тип позиций для показа статисики
    :return: Клаиватура для выбора периода
    """
    print('keyboards.py->get_statistics_period_keyboard', f'#{frameinfo.lineno}', 'Вывод клавиатуры периода показа статистики')
    period_keyboard = InlineKeyboardMarkup(row_width=2)
    all_time = InlineKeyboardButton('За всё время', callback_data='all_time')
    month = InlineKeyboardButton('За месяц', callback_data='month')
    back = InlineKeyboardButton('⬅ Назад️', callback_data=positions_type)

    period_keyboard.add(all_time, month, back)

    return period_keyboard


def get_month_slider(request_type: str, year=None, month=None) -> InlineKeyboardMarkup:
    frameinfo = getframeinfo(currentframe())
    """
    Клавиатура для выбора месяца для показа статистики
    :param request_type: Тип запрашиваемой статистики
    :param year: Год
    :param month: Месяц
    :return: Клаиватура для выбора месяца
    """
    print('keyboards.py->get_month_slider', f'#{frameinfo.lineno}')
    now = datetime.datetime.now()
    if year is None:
        year = now.year
    if month is None:
        month = now.month
    month_slider = InlineKeyboardMarkup(row_width=3)
    prev = InlineKeyboardButton('<<', callback_data=";".join(['prev_slide', str(month), str(year)]))
    empty = InlineKeyboardButton(module.month_name(int(month)) + " " + str(year),
                                 callback_data=";".join(['current_month', str(month), str(year)]))
    nex = InlineKeyboardButton('>>', callback_data=";".join(['next_slide', str(month), str(year)]))
    back = InlineKeyboardButton('⬅ Назад', callback_data=request_type)
    month_slider.add(prev, empty, nex, back)

    return month_slider
