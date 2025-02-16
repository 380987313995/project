# Написати клас Cat, створити атрибути size, color, cat_type.
# 2. При створенні об'єкта класу передавати в конструктор color та cat_type, які записуються у
# відповідні атрибути.
# 3. Зробити метод set_size, коли self.cat_type це “indoor”, то self.size = 'small' інакше
# self.size='undefined'. Протестуйте різні варіанти.
# 4. Створити клас Tiger, успадкований від класу Cat.
# 5. Перевизначити метод set_size таким чином, щоб якщо self.cat_type це 'wild', то self.size =
# ‘big’ інакше self.size=’undefined’.

# class Cat:
#     def __init__(self,size,color,cat_type,*args):
#         self.size=size
#         self.color=color
#         self.cat_type=cat_type
#     def set_size(self):
#         if self.cat_type=='indoor':
#             self.size='small'
#         else:
#             self.size='undefined'

# class Tiger(Cat):
#     def __init__(self,size,color,cat_type,age):
#         super().__init__(size,color,cat_type)
#         self.age=age
#
#     def set_size(self):
#         if self.cat_type=='wild':
#             self.size='big'
#         else:
#             self.size='undefined'
#
# Cat2=Cat('bh','vdvd','indoor','dvv','jhbj')
# Cat1=Tiger('big','grey','wild','6')
# Cat2.set_size()
# Cat1.set_size()
# print(Cat1.size)
# print(Cat2.size)


'''1. Написати клас, який описує користувача (class User), зробити йому приватний атрибут age,
який передається в конструктор, публічний атрибут name, який також передається в
конструктор.
2. Написати getter та setter для атрибуту age.
3. Додати до setter перевірку на валідний вік (не від’ємне, ціле число).'''

class User:
    def __init__(self,age,name):
        self.__age=age
        self.name=name
    def getter(self):
        return self.__age
    @property
    def setter():

        if  type(age) in int:
            self.__age = value

        else:
            raise ValueError('vvedit 4uslo')

variant=User(25,'igor')



variant.setter(36)
print(variant.getter())