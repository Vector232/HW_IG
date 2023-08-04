import types


def flat_generator(list_of_list):
    # Не, ну, а что?
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
    
    data = tishka_flatten(list_of_list)
    for i in data:
        yield i 

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()