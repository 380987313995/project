# country_capital={'Ukraine':'Kiev','England':'London','Italy':'Milan','Germany':'Berlin'}
# print(country_capital.pop('Ukraine')) #pop vudalyae key i vertae znachennya


# print(country_capital)
# print(country_capital.popitem())#povertae jstanni key i zna4ennya

# country_capital.update({'Spain':'Madrid'})  #update- dodae ostanni element
# print(country_capital)
#
#
# values_of_country_capital=country_capital.values()  #povertae zna4ennia
# print(values_of_country_capital)
#
# keys_of_country_capital=country_capital.keys()   #keys vertae keys
# print(keys_of_country_capital)

# print(country_capital.get('England'))#povertae zna4ennya
# print(country_capital.setdefault('England'))


# empty_dict: dict={}
# days_name=['monday','tuesday','wensday']
# number_days=['first','second','third']
# new_dict=empty_dict.fromkeys(days_name,'days')
# print(new_dict)


# names=['Igor','Tanya','Lena','Igor','Tanya']
# answer={}
# for n in names:
#     if n in answer.keys():
#         answer[n]+=1
#     else:
#         answer[n]=1
# print(answer)

# Аналогічно до завдання 1, тільки словник d = {‘a’:3, ‘b’: ‘hello’, ‘c’:4, ‘d’:-3}

# d = {'a':2, 'b': 'hello', 'c':6, 'd':99}
# b=list(d.values())
#
#
# for x in b:
#     if type(x)==str:
#         b.remove(x)
#
#
#         print(max(b))
#
#     #     b.remove(y)
# # print(y)
movies = {
'The Hateful Eight': 2015,
'Inglourious Basterds': 2009,
'Death Proof': 2007
}
find_movie = input('Type a movie: ')
print(movies.get(find_movie.replace(("'",' ')('')),('Not found')))




