import sys


# Функция вывода индекса минимального по модулю отрицательного числа
def index_min():
    n = int(input("Введите размер массива: "))
    array = []
    print("Введите числа:")
    # Заполняем пустой массив
    for i in range(n):
        array.append(int(input()))
    index_min_abs_neg = -1
    min_abs_neg = sys.maxsize
    # Проверяем члены массива на удовлетворения заданным условиям
    for i in range(n):
        if (array[i] < 0) and (abs(array[i]) <= min_abs_neg):
            index_min_abs_neg = i
            min_abs_neg = abs(array[i])
    print(index_min_abs_neg)


# Функция перекрытия строки
def overlapping_strings():
    origin_str = input("Введите оригинальную строку: ")
    overlapping_str = input("Введите строку для перекрытия: ")
    num_of_char = int(input("Введите кол-во символов для перекрытия строки: "))
    position = int(input("Введите позицию в оригинальной строке: "))
    # Создаём перекрытую строку на основе оригинальной
    result_str = origin_str[:position - 1] + overlapping_str[:num_of_char] + origin_str[position + num_of_char - 1:]
    print(result_str)


task = int(input("Введите задание, которое следует выполнить: 1 или 2? \n"
                 "1.Дан одномерный целочисленный массив порядка N. Найти позицию наименьшего по модулю отрицательного\n"
                 "  элемента массива. Если таких элементов несколько, указать номер последнего встреченного.\n"
                 "  Если таких элементов нет, вывести значение –1.\n"
                 "2.Перекрытие строк. Функция перекрывает символы строки, заданным количеством символов\n"
                 "  другой строки, начиная с заданной позиции.\n"))
if task == 1:
    index_min()
elif task == 2:
    overlapping_strings()
else:
    print("Введено неверное значение!")