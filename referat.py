# Задание на работу с файлами
a = 0
with open('referat.txt', 'r', encoding='utf-8') as f:
    my_file = f.read()
    my_file_1 = my_file.replace('\n', ' ')
    print(f'Количество символов в реферате = {len(my_file_1)}')
    
    # Подсчитаем количество слов в тексте
    my_file_2 = my_file_1.split(' ')
    print(f'Количество слов в реферате = {len(my_file_2)}')

# Заменим точки в тексте на восклицательные знаки и сохраним в новом файле
with open('referat_2.txt', 'w', encoding='utf-8') as f_2:
    my_file = my_file.replace('.','!')
    f_2.write(my_file)
    print('Запись модифицированного referat.txt прошла успешна')