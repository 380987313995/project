# class Parser:
#     def __init__(self):
#         pass
#     def convert_type(self,value_str):
#         result=0
#         if isinstance(value_str,str):
#             if '.' in value_str:
#                 result=float(value_str)
#             else:
#                 result=int(value_str)
#         return result
#     def parse(self,expression):
#         packed_values=tuple(expression.split())
#         if len(packed_values)<3:
#             print('Wrong identation,check your expression')
#             return 0,0,'+'
#         a,op,b=packed_values
#         return self.convert_type(a),self.convert_type(b),op
# class Core:
#     def __init__(self):
#         self.parser=Parser()
#         self.functions={"+":lambda a,b:a+b,
#                         '-':lambda a,b:a-b,
#                         '*':lambda a,b:a*b,
#                         '/':lambda a,b:a/b,
#                         '**':lambda a,b:a**b}
#
#     def calculate(self,expression):
#         a,b,op=self.parser.parse(expression)
#         result=self.functions.get(op)(a,b)
#         return  result
# class Interface:
#     def __init__(self):
#         self.core=Core()
#     def run_calculator(self):
#         while True:
#             print("Enter your expression: eg. '2+2':")
#             result =self.core.calculate(input())
#             print('Result:',result)
#             print('='*15)
# if __name__=="__main__":
#     calculator=Interface()
#     calculator.run_calculator()
from abstraction import *
class Parser:
    def __init__(self):
        pass

    def convert_type(self, value_str):
        result = 0
        if isinstance(value_str, str):
            if '.' in value_str:
                result = float(value_str)
            else:
                result = int(value_str)
        return result

    def parse(self, expression):
        # Розбиваємо вираз на список значень
        packed_values = expression.split(',')
        # Перетворюємо кожне значення в числовий тип
        return [self.convert_type(val.strip()) for val in packed_values]


class ListOperations:
    def __init__(self):
        self.parser = Parser()

    def calculate(self, expression):
        # Перетворюємо вираз у список чисел
        values = self.parser.parse(expression)
        return values

    def calculated(self, values, operation):
        if operation == 'max':
            return max(values)
        elif operation == 'min':
            return min(values)
        elif operation == 'sum':
            return sum(values)
        elif operation == 'product':
            result = 1
            for v in values:
                result *= v
            return result
        else:
            return "Invalid operation"


class Interface:
    def __init__(self):
        self.listoperations = ListOperations()

    def run_calculator(self):
        while True:
            print("Enter your expression (e.g., '1, 2, 3, 4'):")
            expression = input()

            # Перетворюємо вираз у список чисел
            values = self.listoperations.calculate(expression)
            if not values:
                print("Invalid input. Please enter a list of numbers.")
                continue

            print("Choose an operation (max, min, sum, product):")
            operation = input()

            # Виконуємо обрану операцію
            result = self.listoperations.calculated(values, operation)

            print(f"Result: {result}")
            print("=" * 15)


if __name__ == "__main__":
    calculator = Interface()
    calculator.run_calculator()
