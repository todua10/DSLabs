# Сортировка выбором
def selection_sort(list1):
    for i in range(len(list1)):

        # Исходно считаем наименьшим первый элемент неотсортированной части списка
        min_val_index = i
        # Проводим поиск минимального элемента в неотсортированной части списка
        for j in range(i + 1, len(list1)):
            # Пропускаем отрицательные элементы
            if list1[j] < 0:
                continue
            if list1[j] < list1[min_val_index]:
                min_val_index = j
        # Минимальный элемент меняем с последним элементом отсортированной части списка
        list1[i], list1[min_val_index] = list1[min_val_index], list1[i]


# Сортировка слиянием
def merge_sort(list2):
    if len(list2) > 1:
        mid = len(list2) // 2
        left = list2[:mid]
        right = list2[mid:]

        # Рекурсивный вызов на каждую половину
        merge_sort(left)
        merge_sort(right)

        # Два итератора для обхода двух половин
        i = 0
        j = 0

        # Итератор для главного списка
        k = 0

        # Массивы для индексов и отрицательных значений
        Index_negative_val = []
        Negative_val = []

        while i < len(left) and j < len(right):
            if left[i] < 0:
                Index_negative_val.append(i)
                Negative_val.append(left[i])
            if right[j] < 0:
                Index_negative_val.append(j)
                Negative_val.append(right[j])
            if left[i] < right[j]:
                # Используется значение из левой половины
                list2[k] = left[i]
                # Инкремент итератора левой половины
                i += 1
            else:
                # Используется значение из правой половины
                list2[k] = right[j]
                # Инкремент итератора правой половины
                j += 1
            # Инкремент главного списка
            k += 1

        # Для всех оставшихся значений
        while i < len(left):
            if left[i] < 0:
                Index_negative_val.append(i)
                Negative_val.append(left[i])
            list2[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            if right[j] < 0:
                Index_negative_val.append(j)
                Negative_val.append(right[j])
            list2[k] = right[j]
            j += 1
            k += 1


# Создаем неотсортированный список
example_list1 = [56, 41, -12, 31, -1, 24, 2, 101, -18]
# Сортируем список выбором
example_list2 = example_list1.copy()
selection_sort(example_list2)
# Сортируем список слиянием
example_list3 = example_list1.copy()
merge_sort(example_list3)
# Создаем копию отсортированного списка без отрицательных элементов
for i in example_list3.copy():
    if i < 0:
        example_list3.remove(i)
# Возвращаем отрицательные элементы на их первоначальные индексы
for i in example_list1:
    if i < 0:
        a = example_list1.index(i)
        example_list3.insert(a, i)

print(example_list2)
print(example_list3)
