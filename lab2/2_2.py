from typing import Tuple, List, Any

#  var a = m.First();
#  var a = m.Last();
#  var a = m.Max();
#  var a = m.Min();
#  var a = m.Sum();
#  var a = m.Average(); // среднее арифметическое
#  var f = m.Contains(2); // проверка наличия элемента


class CustomArray:

    def __init__(self, array: Tuple | List):
        self.array = array

    def first(self) -> Any:
        return self.array[0]

    def last(self) -> Any:
        return self.array[-1]

    def max(self) -> Any:
        max_item = self.array[0]
        for item in self.array[1:]:
            if item > max_item:
                max_item = item

        return max_item

    def min(self) -> Any:
        min_item = self.array[0]
        for item in self.array[1:]:
            if item < min_item:
                min_item = item

        return min_item

    def sum(self) -> Any:
        sum_item = 0
        for item in self.array:
            sum_item += item
        return sum_item

    def average(self) -> Any:
        sum_array = self.sum()
        return sum_array / len(self.array)

    def contains(self, numb: int) -> bool:
        return numb in self.array


if __name__ == '__main__':
    a = [1, 2, 3, -1, 4, 3]
    m = CustomArray(a)

    print(a)

    print('first', m.first())
    print('last', m.last())
    print('max', m.max())
    print('min', m.min())
    print('sum', m.sum())
    print('average', m.average())
    print('contains 2', m.contains(2))
    print('contains 20', m.contains(20))
