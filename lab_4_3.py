# Класс, описывающий хеш-таблицу
class HashTable():
    def __init__(self, size):
        self.__hash_table = [[] for i in range(size)]
        self.__size = size

    # Хеш-функция
    def __hash(self, number):
        # Метод середины квадрата
        number *= number
        number >>= 11
        return number % self.__size

    # Метод добавления числа в таблицу
    def hash_number(self, number):
        self.__hash_table[self.__hash(number)].append(number)

    # Метод поиска числа
    def search(self, number):
        if number in self.__hash_table[self.__hash(number)]:
            print(f"{self.__hash(number)}: {self.__hash_table[self.__hash(number)]}")
        else:
            print(None)

    # Метод вывода таблицы
    def show(self):
        for i in range(self.__size):
            if self.__hash_table[i]:
                print(f"{i}: {self.__hash_table[i]}")


with open("numbers.txt", 'r') as f:
    numbers = f.read().split()

my_hash = HashTable(10 * len(numbers) ** 2)

for num in numbers:
    my_hash.hash_number(int(num))

my_hash.search(222)

my_hash.show()
