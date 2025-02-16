# "Уявімо, що ми створюємо систему для обробки замовлень в ресторані. Нам потрібно створити два класи:
# Клас Dish — представляє страву в меню ресторану. Він має:
# Атрибути: name (назва страви), price (ціна страви).
# Метод get_info(), який повертає інформацію про страву (назва та ціна).
#
# Клас Order — представляє замовлення клієнта. Він має:
# Атрибути: order_number (номер замовлення), dishes (список обраних страв), total_price (загальна ціна замовлення).
# Методи:
# add_dish(dish) — додає страву до замовлення.
# get_total_price() — обчислює загальну вартість усіх страв у замовленні.
# get_order_info() — повертає інформацію про номер замовлення та список всіх страв у замовленні.
#
# Опис класів:
# Dish:
# Створюється зі значеннями name і price.
# Метод get_info() повертає рядок з інформацією про страву.
#
# Order:
# Створюється з номером замовлення та порожнім списком страв.
# Метод add_dish(dish) додає нову страву до списку.
# Метод get_total_price() підсумовує ціни всіх страв у списку.
# Метод get_order_info() виводить інформацію про замовлення, включаючи список страв."

# class Dish:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def get_info(self):
#         print('Name:',self.name,'price:',self.price)
#
# class Order:
#     def __init__(self, order_number):
#         self.order_number = order_number
#         self.dishes = []
#         self.total_price=0
#     def add_dish(self,dish):
#         self.dishes.append(dish)
#         self.total_price+=dish.price
#     def get_total_price(self):
#         print('Total:',self.total_price)
#     def get_order_info(self):
#         print ('Order:',self.order_number)
#         for dish in self.dishes:
#             print(dish.name)
#
# d1=Dish('Pizza',20)
# d2=Dish('Pizza',10)
# o1=Order(1)
# o1.add_dish(d1)
# o1.add_dish(d2)
# o1.get_order_info()
# o1.get_total_price()

# "Умова задачі:
# Створіть систему для роботи з бібліотекою. У бібліотеці є кілька книг, і клієнти можуть їх позичати.
# Клас Book (Книга):
# Атрибути:
# title (назва книги, рядок),
# author (автор книги, рядок),
# is_borrowed (булевий атрибут, що вказує, чи позичена книга).
# Методи:
# get_info() — повертає інформацію про книгу (назва, автор, статус позики).
# borrow() — позичає книгу (якщо книга не позичена).
# return_book() — повертає книгу (якщо книга була позичена).

# Клас Library (Бібліотека):
# Атрибути:
# books (список книг у бібліотеці).
# Методи:
# add_book(book) — додає книгу до бібліотеки.
# show_books() — виводить інформацію про всі книги в бібліотеці.
# borrow_book(book_title) — позичає книгу за назвою.
# # return_book(book_title) — повертає книгу за назвою

class Book:
    def __init__(self,title,author,is_borrowed=False):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    def get_info(self):
        return self.title,self.author,self.is_borrowed

    def borrow(self):
        pass
    def return_book(self):
        pass

    
class Library():
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def show_books(self):
        return [str(book) for book in self.books]

    def borrow_book(self,book_title):
        pass
        
    def return_book(self,book_title):
        pass
b=Book('Title','Autor',True)
a=Library()
a.add_book(b)
print(a.show_books())