# class Addition:
#     name='h'
#     # Параметризований конструктор
#     def __init__(self, f, s=None):
#         self.first = f
#         self.second = s
#
#     def display(self):
#         print("First number = " + str(self.first))
#         print("Second number = " + str(self.second))
#         print("Addition of two numbers = " + str(self.answer))
#
#     def calculate(self):
#         if not self.second :
#             self.second=self.first
#         self.answer = self.first + self.second
#
#
# obj=Addition('a','m')
# obj.calculate()
# obj.display()
#
#
# print(Addition.x)
# class Data:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Database:
#     Dani=[]
#     def read_data(self):
#         if self.__dict__.get('name')==25:
#             self.write_data()
#             print(self.Dani)
#     def write_data(self):
#
#         attributes = [self.name, self.age]
#         for attr in Data():
#             Database.Dani.append(attr)
#
# a=Database(25,6)
# a.read_data()

class  P:
    def __init__(self,name):
        self.name=name

    def fff(self):
        return self.name
class B(P):
    def __init__(self):
        pass


a=B()
print(a.fff())