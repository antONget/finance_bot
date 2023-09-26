import os
from unicodedata import name
from inspect import currentframe, getframeinfo

from sqlalchemy import create_engine, Integer, String, REAL, ForeignKey, Column, exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

BDPATH = 'botdb.db'

base = declarative_base()
engine = create_engine('sqlite:///botdb.db?check_same_thread=False', echo=False)
session = sessionmaker(bind=engine)()


# Инициализация таблиц базы и заполение базы, если она не создана

class Users(base):
    print('module.py->Users', 'создаем таблицу "user" в базе данных')
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_chat_id = Column(String, nullable=False, unique=True)


class Account(base):
    print('module.py->Accaunt')
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    type = Column(String(10), nullable=False)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('expense_categories.id'))
    price = Column(REAL, nullable=False)
    day = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)


class IncomeCategories(base):
    print('module.py->IncomeCategories')
    __tablename__ = 'income_categories'

    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False, unique=True)


class ExpenseCategories(base):
    print('module.py->ExpenseCategories')
    __tablename__ = 'expense_categories'

    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False, unique=True)
    limit = Column(REAL, nullable=False)


if not os.path.exists(BDPATH):
    base.metadata.create_all(engine)
    # категории доходы
    session.add(IncomeCategories(name="Заработная плата"))
    session.add(IncomeCategories(name="Премия"))
    session.add(IncomeCategories(name="Переводы"))
    session.add(IncomeCategories(name="Прибыль"))
    session.add(IncomeCategories(name="Кешбек"))
    session.add(IncomeCategories(name="Прочее"))

    session.add(ExpenseCategories(name="Супермаркеты", limit=1000.0))
    session.add(ExpenseCategories(name="Кафе/рестораны", limit=1000.0))
    session.add(ExpenseCategories(name="Транспорт", limit=1000.0))
    session.add(ExpenseCategories(name="Одежда и акссесуары", limit=1000.0))
    session.add(ExpenseCategories(name="Товары для дома", limit=1000.0))
    session.add(ExpenseCategories(name="Здоровье и красота", limit=1000.0))
    session.add(ExpenseCategories(name="Отдых и развлечения", limit=1000.0))
    session.add(ExpenseCategories(name="Недвижимость, коммунальные платежи", limit=1000.0))
    session.add(ExpenseCategories(name="Прочее", limit=1000.0))

    session.commit()


# Функции для работы с базой данных


def add_user(name: str, chat_id: str):
    """
    Добавление нового пользователя в базу
    :param name: Имя пользователя
    :param chat_id: Уникальный id пользователя в telegram
    """
    print('module.py->add_user', 'Добавление нового пользователя в базу')
    if not has_user(chat_id):
        session.add(Users(user_name=name, user_chat_id=chat_id))
        session.commit()


def has_user(chat_id: str) -> bool:
    """
    Проверка наличия пользователя в базе
    :param chat_id: Уникальный id пользователя в telegram
    :return: True или False в зависимости от того, найден ли пользователь с таким id
    """
    print('module.py->has_user', 'Проверка наличия пользователя в базе')
    is_exists = session.query(exists().where(Users.user_chat_id == chat_id)).scalar()
    return is_exists


def get_user_id(chat_id: str) -> int:
    """
    Получить id в базе по id в telegram
    :param chat_id: Уникальный id пользователя в telegram
    :return: id в базе данных
    """
    print('module.py->get_user_id', 'Получение id в базе по id в telegram')
    user = session.query(Users).filter_by(user_chat_id=chat_id).one()
    return user.id


def get_category_name(id: int, position_type: str) -> str:
    """
    Получить название категории по id
    :param id: id категории в базе данных
    :param position_type: Тип категории
    :return: Наименование категории
    """
    print('module.py->get_category_name', '#123', 'Получить название категории по id')
    name = ''
    if position_type == 'income':
        name = session.query(IncomeCategories.name).filter(IncomeCategories.id == id).one()[0]

    if position_type == 'expense':
        name = session.query(ExpenseCategories.name).filter(ExpenseCategories.id == id).one()[0]

    return name


def get_categories(position_type: str) -> list:
    """
    Получить список категорий по типу
    :param position_type: Тип категории
    :return: Список категорий
    """
    print('module.py->get_categories', 'Получить список категорий по типу', f'{position_type}')
    categories = []
    if position_type == 'income':
        categories = list(session.query(IncomeCategories.name).all())

    if position_type == 'expense':
        categories = list(session.query(ExpenseCategories.name).all())

    return categories

def del_position(name_cat):
    """
    Удаление категории
    """
    print('module.py->del_position', 'Удаление выбранной категории')
    i = session.query(ExpenseCategories).filter(ExpenseCategories.name == name_cat).one()
    session.delete(i)
    session.commit()

def add_position(position: Account):
    """
    Добавить объект позиции в базу данных
    :param position: Объект строки с информацией о позиции
    """
    print('module.py->add_position', '#156', 'Добавить объект позиции в базу данных')
    session.add(position)
    session.commit()

def add_row_table(name_cat):
    '''
    Добавление новой категории в таблицу расходов
    '''
    session.add(ExpenseCategories(name=name_cat, limit=1000))
    session.commit()

def edit_limit(type_cat, name_cat, new_limit):
    frameinfo = getframeinfo(currentframe())
    '''
    правка лимита категории
    '''
    print('module.py->edit_limit', f'#{frameinfo.lineno}', 'Изменение лимита категории')
    if type_cat == 'expense':
        edit_cat_limit = session.query(ExpenseCategories).filter(ExpenseCategories.name==name_cat).first()
    else:
        edit_cat_limit = session.query(IncomeCategories).filter(IncomeCategories.name==name_cat).first()
    if (edit_cat_limit != None):
        edit_cat_limit.limit = new_limit
        session.commit()

def get_positions(chat_id, positions_type: str, month=None, year=None) -> (int, int):
    """
    Получить сумму стоимостей позиций и их количество
    :param chat_id: Уникальный id пользователя в telegram
    :param positions_type: Тип позиций
    :param month: Месяц
    :param year: Год
    :return: Суммарная стоимость позиций, количество позиций
    """
    print('module.py->get_positions')
    user_id = get_user_id(chat_id)
    if month is not None and year is not None:
        price = session.query(Account.price).filter(Account.user_id == user_id, Account.type == positions_type,
                                                    Account.month == month, Account.year == year).all()
        count = session.query(Account).filter(Account.user_id == user_id, Account.type == positions_type,
                                              Account.month == month, Account.year == year).count()
    else:
        price = session.query(Account.price).filter(Account.user_id == user_id, Account.type == positions_type).all()
        count = session.query(Account).filter(Account.user_id == user_id, Account.type == positions_type).count()
    all_price = sum_price(price)

    return all_price, count


def get_categories_positions(chat_id: str, positions_type: str, month=None, year=None) -> dict:
    """
    Получить сумму позиций по категориям
    :param chat_id: Уникальный id пользователя в telegram
    :param positions_type: Тип позиций
    :param month: Месяц
    :param year: Год
    :return: Словарь, где ключ - категория, значение - суммарная стоимость позиций
    """
    print('module.py->get_categories_positions')
    categories_dict = {}
    id = get_user_id(chat_id)
    categories = get_categories(positions_type)
    if month is None and year is None:
        for i in range(len(categories)):
            categories_dict[str(categories[i][0])] = [
                sum_price(session.query(Account.price).filter(Account.user_id == id, Account.type == positions_type,
                                                              Account.category_id == i + 1).all()),
                session.query(Account).filter(Account.user_id == id,
                                              Account.type == positions_type,
                                              Account.category_id == i + 1).count()
            ]
    else:
        for i in range(len(categories)):
            categories_dict[str(categories[i][0])] = [
                sum_price(session.query(Account.price).filter(Account.user_id == id, Account.type == positions_type,
                                                              Account.category_id == i + 1,
                                                              Account.month == month, Account.year == year).all()),
                session.query(Account).filter(Account.user_id == id,
                                              Account.type == positions_type,
                                              Account.category_id == i + 1,
                                              Account.month == month,
                                              Account.year == year).count()
            ]

    return categories_dict


def get_data(chat_id: str, positions_type: str, month=None, year=None) -> dict:
    """
    Получение информации для формирования таблицы
    :param chat_id: Уникальный id пользователя в telegram
    :param positions_type: Тип позиций
    :param month: Месяц
    :param year: Год
    :return: Словарь с именами, категориями, датами и стоимостью запрашиваемых позиций за запрашивамое время
    """
    print('module.py->get_data')
    user_id = get_user_id(chat_id)
    data_dict = {}
    if month is None and year is None:
        names = list(session.query(Account.name).filter(Account.user_id == user_id,
                                                        Account.type == positions_type).all())
        categories = list(session.query(Account.category_id).filter(Account.user_id == user_id,
                                                                    Account.type == positions_type).all())
        prices = list(session.query(Account.price).filter(Account.user_id == user_id,
                                                          Account.type == positions_type).all())
        days = list(session.query(Account.day).filter(Account.user_id == user_id,
                                                      Account.type == positions_type).all())
        months = list(session.query(Account.month).filter(Account.user_id == user_id,
                                                          Account.type == positions_type).all())
        years = list(session.query(Account.year).filter(Account.user_id == user_id,
                                                        Account.type == positions_type).all())

        dates = []

        for i in range(len(names)):
            names[i] = names[i][0]
            categories[i] = get_category_name(categories[i][0], positions_type)
            prices[i] = prices[i][0]
            dates.append(f'{days[i][0]}/{months[i][0]}/{years[i][0]}')

        data_dict['Наименование'] = names
        data_dict['Категория'] = categories
        data_dict['Сумма'] = prices
        data_dict['Дата'] = dates

    else:
        names = list(session.query(Account.name).filter(Account.user_id == user_id,
                                                        Account.type == positions_type,
                                                        Account.month == month,
                                                        Account.year == year).all())
        categories = list(session.query(Account.category_id).filter(Account.user_id == user_id,
                                                                    Account.type == positions_type,
                                                                    Account.month == month,
                                                                    Account.year == year).all())
        prices = list(session.query(Account.price).filter(Account.user_id == user_id,
                                                          Account.type == positions_type, Account.month == month,
                                                          Account.year == year).all())
        days = list(session.query(Account.day).filter(Account.user_id == user_id,
                                                      Account.type == positions_type, Account.month == month,
                                                      Account.year == year).all())

        dates = []

        for i in range(len(names)):
            names[i] = names[i][0]
            categories[i] = get_category_name(categories[i][0], positions_type)
            prices[i] = prices[i][0]
            dates.append(f'{days[i][0]}/{month}/{year}')

        data_dict['Наименование'] = names
        data_dict['Категория'] = categories
        data_dict['Сумма'] = prices
        data_dict['Дата'] = dates

    return data_dict


# Служебные функции и классы для работы бота и базы данных

class StatisticsRequest(object):
    """
    Запрос статистики, хранящий в себе параметры, необходимые для вывода нужной статистики
    """
    print('module.py->StatisticsRequest')
    def __init__(self, positions_type, request_type=None, month=None, year=None):
        self.positions_type = positions_type
        self.request_type = request_type
        self.month = month
        self.year = year


def sum_price(positions) -> float:
    """
    Вывод суммы позиций
    :param positions: Список позиций
    :return: Суммарная стоимость
    """
    print('module.py->sum_price')
    all_price = 0
    for i in positions:
        all_price += float(i[0])
    return all_price


def get_medium(current: float, all_count: float) -> float or str:
    """
    Возвращает среднюю стоимость позиций
    :param current: Стоимость всех позиций
    :param all_count: Количество позиций
    :return: Средняя стоимость или строка с прочерком в случае ошибки
    """
    print('module.py->get_medium')
    if not all_count == 0:
        return round(current / all_count, 2)
    else:
        return '-'


def month_name(number: int) -> str:
    """
    Возвращает название месяца
    :param number: Номер месяца
    :return: Название
    """
    print('module.py->month_name')
    if number == 1:
        return "январь"
    elif number == 2:
        return "февраль"
    elif number == 3:
        return "март"
    elif number == 4:
        return "апрель"
    elif number == 5:
        return "май"
    elif number == 6:
        return "июнь"
    elif number == 7:
        return "июль"
    elif number == 8:
        return "август"
    elif number == 9:
        return "сентябрь"
    elif number == 10:
        return "октябрь"
    elif number == 11:
        return "ноябрь"
    elif number == 12:
        return "декабрь"
