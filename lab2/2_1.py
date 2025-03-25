from typing import Tuple, List

#  Array.Reverse(m); // реверс элементов массива
#  Array.Resize(ref m, 4); // изменение размера до 4 элементов
#  Array.Copy(m, i, m1, 0, j); // копирование со i-го по j-й элемент в позицию 0


class CustomArray:

    @staticmethod
    def reverse(array: Tuple | List) -> Tuple | List:
        """
        Реверс элементов массива
        :param array: массив
        :return: Реверс массив
        """
        return array[::-1]

    @staticmethod
    def resize(array: Tuple | List, numb_count) -> Tuple | List:
        return array[:numb_count]

    @staticmethod
    def copy(
        array: Tuple | List,
        start_index: int,
        array_for_copy: Tuple | List,
        position_to_copy: int,
        end_index: int
    ) -> Tuple | List:
        slice_array = array_for_copy[start_index:end_index]
        return array[:position_to_copy] + slice_array + array[position_to_copy:]


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = ['a', 'b']

    print('reverse', CustomArray.reverse(a))
    print('resize', CustomArray.resize(a, 2))
    print('copy', CustomArray.copy(a, 0, b, 1, len(b),))
