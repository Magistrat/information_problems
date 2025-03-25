class MyList:
    def __init__(self, initial_data=None):
        """
        Инициализация списка. Можно передать начальные данные в виде итерируемого объекта.
        """
        if initial_data is None:
            self._data = []
        else:
            self._data = list(initial_data)

    def add(self, item):
        """
        Добавляет элемент в конец списка.
        """
        self._data.append(item)

    def insert(self, index, item):
        """
        Вставляет элемент в указанную позицию списка.
        """
        self._data.insert(index, item)

    def remove(self, item):
        """
        Удаляет первое вхождение указанного элемента из списка.
        Если элемент не найден, ничего не происходит.
        """
        if item in self._data:
            self._data.remove(item)

    def __str__(self):
        """
        Возвращает строковое представление списка.
        """
        return ' '.join(map(str, self._data))

    # Для удобства использования можно добавить другие методы, например:
    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __contains__(self, item):
        return item in self._data


# Примеры использования:
if __name__ == "__main__":
    # 1. Создание и инициализация списка заданными значениями из массива
    list1 = MyList([8, 3, 2])
    print("list:", list1)  # list: 8 3 2

    # 2. Добавление элемента в конец списка
    list1.add(5)
    print("list:", list1)  # list: 8 3 2 5

    # 3. Вставка элемента в указанную позицию списка
    list1.insert(1, 5)
    print("list:", list1)  # list: 8 5 3 2 5

    # 4. Удаление первого вхождения элемента
    list2 = MyList([8, 4, 2, 4])
    list2.remove(4)
    print("list:", list2)  # list: 8 2 4
    