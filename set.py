def collect_numbers():
    numbers = set()
    while len(numbers) < 10:
        try:
            num = int(input("Enter a number: "))
            numbers.add(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers

def sum_collection(collection):
    return sum(collection)

def remove_item(collection, number):
    if number in collection:
        collection.remove(number)
        return number
    else:
        return None

def create_sequential_list():
    return list(range(1, 16))

def duplicate_elements(input_list):
    return [x for x in input_list for _ in range(2)]

def remove_duplicates(input_list):
    return list(set(input_list))

def add_every_third_element(input_list):
    return sum(input_list[2::3])

def sum_first_middle_last(input_list):
    length = len(input_list)
    if length % 2 == 0:
        middle_elements = input_list[length//2 - 1: length//2 + 1]
        middle_sum = sum(middle_elements) / 2
    else:
        middle_sum = input_list[length//2]
    return input_list[0] + input_list[-1] + middle_sum


def find_intersection(set1, set2):
    return set1.intersection(set2)
