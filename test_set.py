import set

def test_collect_numbers(monkeypatch):
    inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    assert set.collect_numbers() == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

def test_sum_collection():
    assert set.sum_collection({1, 2, 3, 4, 5}) == 15

def test_remove_item():
    collection = {1, 2, 3, 4, 5}
    assert set.remove_item(collection, 3) == 3
    assert collection == {1, 2, 4, 5}
    assert set.remove_item(collection, 6) is None

def test_find_intersection():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    assert set.find_intersection(set1, set2) == {3, 4, 5}

def test_create_sequential_list():
    assert set.create_sequential_list() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def test_duplicate_elements():
    assert set.duplicate_elements([1, 2, 3]) == [1, 1, 2, 2, 3, 3]

def test_remove_duplicates():
    assert set.remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]

def test_add_every_third_element():
    assert set.add_every_third_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18

def test_sum_first_middle_last():
    assert set.sum_first_middle_last([1, 2, 3, 4, 5, 6, 7]) == 12
    assert set.sum_first_middle_last([1, 2, 3, 4, 5, 6, 7, 8]) == 13.5


if __name__ == '__main__':
    pytest.main()
