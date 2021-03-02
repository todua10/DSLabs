import sys


def Index_abs_neg():
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


def Overlapping_strings():
    origin_str = input("Введите оригинальную строку: ")
    overlapping_str = input("Введите строку для перекрытия: ")
    num_of_char = int(input("Введите кол-во символов для перекрытия строки: "))
    position = int(input("Введите позицию в оригинальной строке: "))
    result_str = origin_str[:position - 1] + overlapping_str[:num_of_char] + origin_str[position + num_of_char - 1:]
    print(result_str)


task = int(input("Введите задание, которое следует выполнить: 1 или 2? \n"))
if task == 1:
    Index_abs_neg()
elif task == 2:
    Overlapping_strings()
else:
    print("Введено неверное значение!")
