from datetime import date
from typing import List

# 1 задание
x = int(input("Какое задание выполнить 1 или 2?\n"))
if x == 1:
    # класс узла, который хранит текущее значение и указатель на следующий узел
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    # сортировка по наименованию тура
    def sort_by_name():
        list_of_values = [records.first.value, records.first.next.value, records.first.next.next.value]
        list_of_values.sort(key=lambda sold_tour: sold_tour.name)
        records.clear()
        records.first = Node(list_of_values[2], None)
        records.first = Node(list_of_values[1], records.first)
        records.first = Node(list_of_values[0], records.first)
        return

    # сортировка по цене одного дня
    def sort_by_price():
        list_of_values = [records.first.value, records.first.next.value, records.first.next.next.value]
        list_of_values.sort(key=lambda sold_tour: sold_tour.price_rub)
        records.clear()
        records.first = Node(list_of_values[2], None)
        records.first = Node(list_of_values[1], records.first)
        records.first = Node(list_of_values[0], records.first)
        return

    # сортировка по дате заезда
    def sort_by_date():
        list_of_values = [records.first.value, records.first.next.value, records.first.next.next.value]
        list_of_values.sort(key=lambda sold_tour: sold_tour.date_in)
        records.clear()
        records.first = Node(list_of_values[2], None)
        records.first = Node(list_of_values[1], records.first)
        records.first = Node(list_of_values[0], records.first)
        return

    # поиск по одному из полей
    def find_by(val):
        list_of_values = [records.first.value, records.first.next.value, records.first.next.next.value]
        if type(val) is str:
            for m in list_of_values:
                if val in m.name:
                    return m
        elif type(val) is int:
            for j in list_of_values:
                if val == j.price_rub:
                    return j
                elif val == j.date_in.year:
                    return j
                elif val == j.date_in.month:
                    return j
                elif val == j.date_in.day:
                    return j
        elif type(val) is date:
            for k in list_of_values:
                if val == k.date_in:
                    return k
        else:
            return "Неправильно задан элемент"

    # класс односвязного списка
    class LinkedList:
        def __init__(self):
            self.first = None

        def __str__(self):
            if self.first is not None:
                current = self.first
                out = 'LinkedList = ' + str(current.value) + '; '
                while current.next is not None:
                    current = current.next
                    out += str(current.value) + ' '
                return out + ''
            return ''

        def clear(self):
            self.__init__()

    # класс учетной записи о проданном туре
    class SoldTour:

        def __init__(self,
                     name: str,
                     last_name: str,
                     price_rub: int,
                     date_in: List[int],
                     num_of_days: int,
                     fare: int,
                     cur_exchange_rate: float,
                     num_of_cur: int):
            self.name = name
            self.last_name = last_name
            self.price_rub = price_rub
            self.date_in = date(*date_in)
            self.num_of_days = num_of_days
            self.fare = fare
            self.cur_exchange_rate = cur_exchange_rate
            self.num_of_cur = num_of_cur

        def __str__(self):
            return ' '.join((self.name,
                             self.last_name,
                             str(self.price_rub),
                             str(self.date_in),
                             str(self.num_of_days),
                             str(self.fare),
                             str(self.cur_exchange_rate),
                             str(self.num_of_cur)))

    # создание и заполнение односвязного списка данными учетных записей
    records = LinkedList()
    records.first = Node(SoldTour("Incredible Egypt",
                                  "Popov",
                                  7000,
                                  [2015, 7, 9],
                                  8,
                                  3,
                                  14.5,
                                  100), None)
    records.first = Node(SoldTour("Calm Japan",
                                  "Emeev",
                                  9000,
                                  [2014, 5, 15],
                                  12,
                                  5,
                                  23.7,
                                  100), records.first)
    records.first = Node(SoldTour("Mother Russia",
                                  "Smith",
                                  5000,
                                  [2020, 1, 7],
                                  7,
                                  1,
                                  71.2,
                                  100), records.first)
    # тестирование сортировок и вывод сортированных списков
    sort_by_name()
    print(records)
    sort_by_price()
    print(records)
    sort_by_date()
    print(records)
    # тестирование поиска по полю
    print(find_by('Egypt'))
    print(find_by(52000))
    print(find_by(date(2020, 1, 7)))
# 2 задание
else:
    # класс стека
    class Stack:
        arr = []

        def push(self, variable):
            self.arr.append(variable)

        def pop(self):
            return self.arr.pop(len(self.arr) - 1)

    # создание и заполнение стека
    stack = Stack()
    n = int(input("Введите кол-во элементов в стеке:\n"))
    print("Введите числа:")
    for i in range(n):
        a = int(input())
        stack.push(a)

    # извлечение элементов и расчет среднего арифметического
    sum_of_num = 0
    for i in range(n):
        element = stack.pop()
        sum_of_num += element

    average = sum_of_num / n

    # помещение среднего арифметического в пустой стек и вывод стека
    if average % 1 == 0:
        average = int(average)
    stack.push(average)
    print(stack.arr)
