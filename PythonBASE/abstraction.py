# class Parser:
#     def __init__(self):
#         pass
#     def __convert_type(self,value_str):
#         result = 0
#         if isinstance(value_str,str):
#             if '.' in value_str:
#                 result = float(value_str)
#             else:
#                 result = int(value_str)
#         return result
#     def parse(self,expression):
#         a,op,b=tuple(expression.split(' '))
#         return self.__convert_type(a),self.__convert_type(b)
# class Core:
#     def __init__(self):
#         self._parser=Parser()
#         self._function={
#             '+': lambda a, b: a + b,
#             '-': lambda a, b: a - b,
#             '*': lambda a, b: a * b,
#             '/': lambda a, b: a / b,
#         }
#     def calculate(self,expression):
#         a,b,op=self._parser.parse(expression)
#         result=self._function.get(op)(a,b)
#         return result
#
# class Interface:
#     def __init__(self):
#         self._core=Core()
#     def run_calculator(self):
#         while True:
#             print('enter number')
#             expression=input()
#             result=self._core.calculate(expression)
#             print('result:',result)
#             print('_'*10)
#
# # calculator=Interface()
# # calculator.run_calculator()
#
#     print(Parser())
#
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
#     def __init__(self):
#         self.database=Data()
#     user_1 = ["CZ","Orest", 18, "male", 167, 72]
#     user_2 = ["UA", "Ivanka", 28, "female", 160, 50]
#     user_3 = ["USA","John", 25, "male", 187, 92]
#     user_4 = ["PL", "Tomasz", 50, "male", 177, 87]
#     user_5 = ["GB", "Elizabeth", 26, "female", 175, 65]
#     def read_data(self,criteria):
#         self.criteria=criteria
#
#     def write_data(self,element):
#         pass
# class Data:
#     def __init__(self,age):
#         self.age=age
# print(Database())






class Data:
    def __init__(self, country, name, age, gender, height, weight):
        self._data = Database()
        self._country = country
        self._name = name
        self._age = age
        self._gender = gender
        self._height = height
        self._weight = weight
        element = {"country":self._country, "name": self._name, "age": self._age,"gender": self._gender,"height": self._height,"weight": self._weight}
        self._data.write_data(element)
class Database:
    _database = []
    def read_data(self, criteria):
        result = []
        for elem in self._database:
            if elem.get(list(criteria.keys())[0]) == list(criteria.values())[0]:
                result.append(elem)
        return result
    def write_data(self, element):
        self._database.append(element)

user_1 = Data(country="CZ", name="Orest", age=18, gender="male", height=167, weight=72)
user_2 = Data(country="UA", name="Ivanka", age=28, gender="female", height=160, weight=50)
user_3 = Data(country="USA", name="John", age=25, gender="male", height=187, weight=92)
user_4 = Data(country="PL", name="Tomasz", age=50, gender="male", height=177, weight=87)
user_5 = Data(country="GB", name="Elizabeth", age=26, gender="female", height=175, weight=65)

print(Database().read_data(criteria={"age": 25}))

