x = int(input("Какое задание выполнить 1 или 2?\n"))
if x == 1:
    class Queue:
        def __init__(self):
            self.queue = []

        def isEmpty(self):
            return self.queue == []

        def enqueue(self, val):
            self.queue.insert(0, val)

        def dequeue(self):
            return self.queue.pop()

        def size(self):
            return len(self.queue)

    queue = Queue()
    inverse_queue = Queue()
    n = int(input("Сколько элементов вы хотите поместить в очередь?\n"))
    print("Введите числа:")
    for i in range(n):
        value = int(input())
        queue.enqueue(value)

    print(queue.queue)
    for i in range(n):
        inverse_value = queue.dequeue()*(-1)
        inverse_queue.enqueue(inverse_value)

    print(inverse_queue.queue)
else:
    def superset(set1, set2):
        if set1 > set2:
            print(f'Множество {set1} является чистым супермножеством')
        elif set1 == set2:
            print(f'Множества равны')
        elif set1 < set2:
            print(f'Множество {set2} является чистым супермножеством')
        else:
            print('Супермножество не обнаружено')

    set1 = {4, 14, 62, 23, 2}
    set2 = {2, 62, 4}
    set3 = {25, 141, 4, 14, 2, 23, 62}
    set4 = {62, 2, 4}
    set5 = {1, 2, 5}
    superset(set1, set2)
    superset(set1, set3)
    superset(set2, set4)
    superset(set2, set5)