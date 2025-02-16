# class Point:
#     point_list=[]
#     def __init__(self,coord_x=0,coord_y=0):
#         self.move_to(coord_x,coord_y)
#         Point.point_list.append(self)
#     def move_to(self,new_x,new_y):
#         self.x=new_x
#         self.y=new_y
#     def go_home(self):
#         return self.move_to(0,0)
#     def print_list(self):
#         print(Point.point_list)
#
# p1=Point()
# print(p1.go_home())
# p1.print_list()
class BankAccount:
    def __init__(self,account_holder,account_number,account_type,balance=0):
        self.account_holder=account_holder
        self.balance=balance
        self.account_number=account_number
        self.account_type=account_type

    def deposit(self, amount):
        if not type(amount)==(int or float):
            raise TypeError('vvedit 4uslo')
        self.balance = amount +self.balance
        if self.balance<=0:
            raise TypeError('sumamae bytudodatnyoyu')
    def withdraw(self, amount):
        if not type(amount)==(int or float):
            raise TypeError('vvedit 4uslo')
        self.balance = self.balance-amount
        if self.balance<=0:
            raise TypeError('nedostatnyo koshtiv')

    def get_balance(self):
        print('Account balance:',self.balance)
        
    def transfer(self, target_account, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError('Введіть числове значення для переказу')
        if amount > self.balance:
            raise ValueError('Недостатньо коштів для переказу')

        self.withdraw(amount)  # Знімаємо гроші з поточного рахунку
        target_account.deposit(amount)  # Поповнюємо інший рахунок


        



    def get_account_info(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}, Account Type: {self.account_type}, Account Number: {self.account_number}"
p1=BankAccount('Pavlo',5,'debit',1265)
p1.withdraw(2)

print(p1.get_account_info())
p1.get_balance()
p2=BankAccount('sisis',5,'debit',5)


p1.transfer(p2,500)
p1.get_balance()
print(p2.get_account_info())
# "Методи:
# __init__(self, account_holder, account_number, account_type, balance=0) — конструктор класу,
# який ініціалізує атрибути. Баланс за замовчуванням має бути 0.
# deposit(self, amount) — метод для поповнення рахунку. Приймає параметр amount — суму поповнення.
# Якщо сума поповнення від'ємна або дорівнює нулю, вивести повідомлення "Сума поповнення має бути додатною!".
# withdraw(self, amount) — метод для зняття коштів з рахунку. Приймає параметр amount — суму зняття.
# Якщо сума зняття більше за баланс, вивести повідомлення "Недостатньо коштів на рахунку!". Якщо сума
# зняття від'ємна або дорівнює нулю, вивести повідомлення "Сума зняття має бути додатною!".
# get_balance(self) — метод для отримання поточного балансу рахунку.
# get_account_info(self) — метод для виведення всієї інформації про рахунок: ім('я власника, номер рахунку,'
# ' тип рахунку, поточний баланс.)
# transfer(self, target_account, amount) — метод для переказу грошей з одного рахунку на інший.
# Приймає параметри: target_account — об('єкт іншого рахунку та amount — сума переказу. Якщо на рахунку недостатньо '
# 'коштів для переказу, вивести повідомлення "Недостатньо коштів для переказу!".'
# ' Якщо сума переказу від')ємна або дорівнює нулю, вивести повідомлення "Сума переказу має бути додатною!".""