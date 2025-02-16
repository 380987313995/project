# def months_name (month_number:int):
#     months = ['january', 'february', 'march', 'april', 'may',
#               'july', 'august', 'september', 'october', 'november', 'december']
#     try:
#         months_index=abs(int(month_number))-1
#         return months[months_index]
#     except (TypeError,ValueError):
#         return 'Please use only integers'
#     except IndexError:
#         return 'Please use integers between 1 and 12'
#
#
# print(months_name(input('vvedit')))

#
# def answer(x,y):
#     # b = [x, y, z]
#     # a = {x, y, z}
#     try:
#         if len([x,y])==len({x,y}):
#             return True
#         else:
#             return False
#     except TypeError:
#         return 'vvedit 3 arg'
#     finally:
#         return 'vvedit 3 arg'
# #
# print(answer(2,4,5,6,6))

# assert 1==2

'''Завдання 1
Написати функцію, яка приймає параметрами 2 аргументи і повертає результатом їх приватне, де
перший аргумент - ділене, а другий - дільник (перший розділити на другий). Обробити
ZeroDivizionError, повернути 0 і вивести повідомлення про помилку, що на 0 ділити не можна.'''

# def zada4a1(x,y):
#     try:
#         return (int(x)/int(y))
#     except :
#         print('NA 0')
#         return 0
#
# print(zada4a1(input('f'),input('f')))

'''Завдання 2
Написати функцію, яка повертає елемент зі списку за індексом. Приймає 2 аргументи: список та
індекс. Написати обробку виключення - якщо в списку такого індексу немає, вивести
повідомлення про помилку та повернути -1.'''

# def zada4a2(x,y):
#     try:
#         return x[y-1]
#     except IndexError:
#         print(-1)
#         return 'pomylka'
# print(zada4a2(['a','b','c'],6))


# a='hello'
# b=a.split('')
# print(b)
a='a'
print(a is a)