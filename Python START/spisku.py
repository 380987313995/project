# список а = [2, 4, 65, 32, 2, 6, 0, -1, 3]. Вивести всі значення менше 5 у консоль
# a = [2, 4, 65, 32, 2, 6, 0, -1, 3]
# a1=list()
#
# for num in a:
#     if num<5:
#         a1.append(num)
# print(a1)

# palindrom=input('word:\n')
# b=list(palindrom)
# copy_b=b.copy()
# copy_b.reverse()
#
# if b==copy_b:
#     print('good')
# else:
#     print('bad')


# #Є список a = [1, 3, 9, 13, 7, 8, 13, 32, 44, 59, 19].
# # Виведіть всі елементи, які мають менше 6.
# a = [1, 3, 9, 13, 7, 8, 13, 32, 44, 59, 19]
# a1=list()
#
# for num in a:
#     if num<6:
#         a1.append(num)
# print(a1)

# На основі списку a = ['red', 'yellow', 'blue', 'bread']
# Створити список, у якому буде лише слово, зайве у списку a.

a = ['one', 'two']
colors=['ice', 'red', 'blue','green','two']
n=0

# for x in a :
#     b = colors[n]
#     n += 1
#     if x == b:
#         print(x)
for x in a:
    if x==colors[n]:
        print(x)
    else:
        n+=1












