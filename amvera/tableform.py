import os
import pandas as pd


def form_table(id, dictionary: dict):
    """
    Формирование таблицы со статистикой для пользователя
    :param id: Уникальный id пользователя в telegram
    :param dictionary: Словарь с информацией для формирования статистки
    :return:
    """
    print('tableform.py->form_table')
    if os.path.exists(f'/userfiles/tables/{id}.xlsx'):
        os.remove(f'/userfiles/tables/{id}.xlsx')
    table = pd.DataFrame(dictionary)
    print(table)
    # table.to_excel(f'{id}.xlsx', sheet_name='Статистика', index=False)
    # table.to_csv(f'userfiles/tables/{id}.csv')
    table.to_excel(f'userfiles/tables/{id}.xlsx', sheet_name='Статистика', index=False)
