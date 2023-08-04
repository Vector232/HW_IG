# 1. Доработать класс FlatIterator в коде ниже. Должен получиться итератор, 
# который принимает список списков и возвращает их плоское представление, т. е. 
# последовательность, состоящую из вложенных элементов. 
# Функция test в коде ниже также должна отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.main_counter = 0
        self.sub_counter = 0

        self.main_len_list = len(self.list_of_lists)
        self.sub_len_list = None

        return self

    def __next__(self):
        if self.main_counter >= self.main_len_list:
                raise StopIteration
        
        if not self.sub_len_list:
            self.sub_len_list = len(self.list_of_lists[self.main_counter])

        item = self.list_of_lists[self.main_counter][self.sub_counter]

        self.sub_counter += 1
        
        if self.sub_counter >= self.sub_len_list:
            self.sub_counter = 0
            self.main_counter += 1
            self.sub_len_list = None
            
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print([i for i in FlatIterator(list_of_lists_1)])

    test_1()