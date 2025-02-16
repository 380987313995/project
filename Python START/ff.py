# class A:
#     def __init__(self):
#         self.b='bgh'
#
#
#
# class B:
#     def __init__(self):
#         self.A=A()
#     def U(self):
#         print(str(self.A)+str(self.A))
#
#
# x=B().U()


# class printer():
#     ''' Тест @staticmethod '''
#     def not_static_print(self, text = 'Example Text'):
#         print(text)
#     @staticmethod
#     def static_print(self,text = 'Example Text'):
#         print(text)
# # Не создаю никаких экземпляров
# printer.not_static_print(5)
# printer.static_print(None,'Something like this.')
# class Cat:
#     age=5
#     def showname(self):
#         print('my name is',self.name)
# a=Cat()
# a.name='5'
# a.showname()

"""1. Організуйте архітектуру програми “База даних” (псевдо). У ролі бази даних у вас буде
клас Database, який зберігатиме дані у вигляді змінної списку.
2. Клас Database повинен мати методи read_data(criteria), write_data(element).
3. Для елементів даних напишіть клас Data. У цьому випадку ми зберігатимемо дані про
користувачів. Data матиме атрибути: country, name, age, gender, height, weight.
4. У класі Database метод read_data прийматиме на вхід аргумент criteria, який є словником
виду {“age”: 25}, після чого метод поверне окремий список всіх елементів, у яких дана
умова істина.
Підказка: щоб отримати в об'єкта класу значення його атрибуту як у словника, використовуйте
наступний синтаксис: your_class_instance. dict .get('name').
PS: організуйте правильну інкапсуляцію. Ви повинні додавати елементи"""





# class Database:
#     Dani = []
#     def read_data(self):
#         if self.Dani.get('age')==25:
#             pass
#
#     def write_data(self,element):
#         self.element=self.dani
#         Database.Dani.append(element)
# class Data:
#     def __init__(self, name, age):
#         self.dani=Database()
#         self.name=name
#         self.age=age
# a=Data(5,5)
# print(a.__dict__)
# self.dict.get('name')
# a=Data(5,4)
# h=getattr(a,'name')
# print(h)
# database=[]
# def read_data(criteria):
#     result = []
#     for elem in database:
#         if elem.get(list(criteria.keys())[0]) == list(criteria.values())[0]:
#             result.append(elem)
#     return result
# read_data(5)
# a={'d':4,'g':5,'f':7}
# print(a.get('d'))
# Создайте абстрактный класс Transport, который будет содержать абстрактные методы:
# start(): метод для запуска транспортного средства.
# stop(): метод для остановки транспортного средства.
# get_speed(): метод, который возвращает текущую скорость транспортного средства.
# Создайте два класса, наследующих от Transport:
# Car (автомобиль), который реализует все абстрактные методы и имеет дополнительный атрибут — fuel_level (уровень топлива).
# Bicycle (велосипед), который также реализует все абстрактные методы и имеет дополнительный атрибут — gear (скорость велосипеда).
# В классе Car добавьте логику для старта и остановки с учетом уровня топлива. Если топлива недостаточно для старта,
# необходимо вывести сообщение "Не хватает топлива".
# В классе Bicycle реализуйте логику для старта и остановки, учитывая, что велосипед не использует топливо и
# не имеет определенной скорости, а только переключает передачи.
# Напишите пример использования этой системы, где создаются объекты Car и Bicycle, и вызываются их методы.
#
# class Transport:
#     def __init__(self):
#         pass
#     def start(self):
#         pass
#     def stop(self):
#         pass
#     def get_speed(self):
#         pass
# class Car(Transport):
#
#     def fuel_level(self):
# class Bicycle(Transport):
values=input('vvedu:')
def multiply_list(values):
    result = 1
    for value in values:
        result *= value
    return result
c=multiply_list(values)
print(c)