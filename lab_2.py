# 1 задание
class SoldTour:

    def __init__(self, name, last_name, price_rub, date, num_of_days, fare, cur_exchange_rate, num_of_cur):
        self.name = name
        self.last_name = last_name
        self.price_rub = price_rub
        self.date = date
        self.num_of_days = num_of_days
        self.fare = fare
        self.cur_exchange_rate = cur_exchange_rate
        self.num_of_cur = num_of_cur


# 2 задание
class Stack:
    arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        self.arr.pop(len(self.arr) - 1)


stack = Stack()
n = int(input("Введите кол-во элементов в стеке:\n"))
for i in range(n):
    a = int(input("Введите число:\n"))
    stack.push(a)

sum_of_num = 0
for i in range(n):
    sum_of_num += stack.pop()

average = sum_of_num/n
stack.push(average)