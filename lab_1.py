import sys


def Array_abs_neg():
    n = int(input("Введите размер массива: "))
    array = []
    print("Введите числа:")
    for i in range(n):
        array.append(int(input()))
    index_min_abs_neg = -1
    min_abs_neg = sys.maxsize
    for i in range(n):
        if (array[i] < 0) and (abs(array[i]) <= min_abs_neg):
            index_min_abs_neg = i
            min_abs_neg = abs(array[i])
    print(index_min_abs_neg)