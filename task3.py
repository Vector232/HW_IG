class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list 

    
    def __iter__(self):
        # Ну типа... Готовая функция из интернета. Не самая оптимальная, но и задача не стоит.
        def tishka_flatten(data):
            nested = True
            while nested:
                new = []
                nested = False
                for i in data:
                    if isinstance(i, list):
                        new.extend(i)
                        nested = True
                    else:
                        new.append(i)
                data = new
            return data
        
        self.data = tishka_flatten(self.list_of_list)
        self.c = 0
        self.len = len(self.data)
        return self
    
    def __next__(self):
        if self.c >= self.len:
                raise StopIteration
        
        item = self.data[self.c]

        self.c += 1

        return item
      
       


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()