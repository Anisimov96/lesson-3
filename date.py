
# Программа была помещена в виртуальное окружение
from datetime import datetime, date, time, timedelta
import locale # Подключаем модуль локали
# Задание_1 напечатать даты вчера, сегодня, месяц назад
locale.setlocale(locale.LC_TIME, 'Russian_Russia.1251')
dt_now = date.today()
a = dt_now.strftime('%A,%d:%B:%Y')
print(f'Сегодня: {a}')

delta_1 = timedelta(days=1)
yesterday = dt_now - delta_1
b = yesterday.strftime('%A,%d:%B,%Y')
print(f'Вчера: {b}')

# Месяц назад я не уверен, правильно ли делаю, что
# в days указываю 31
delta_2 = timedelta(days=31) 
month_ago = dt_now - delta_2
c = month_ago.strftime('%A,%d:%B,%Y')
print(f'Месяц назад: {c}')

# Задание_2 Превратить строку в объект datetime
str_date = '01/01/17 12:10:03.234567'
str_date_1 = datetime.strptime(str_date, '%d/%m/%y %H:%M:%S.%f')
print(str_date_1)