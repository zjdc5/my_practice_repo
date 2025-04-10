def length_of_list(list):
    """
    Given a list, this function returns the length of the list.
    """
    return len(list)

def get_element(list, index):
    """
    Given a list and an index, this function returns the element in the list at the specified index.
    """
    if len(list) >= 1:
        return list[index]
    else:
        return "Out of bounds."

list1 = [10, 20, 30, 40, 50]
list2 = ['a', 'b', 'c']
list3 = []

print(length_of_list(list1))
print("Expected: 5")

print()

print(length_of_list(list2))
print("Expected: 3")

print()

print(length_of_list(list3))
print("Expected: 0")

print()
print()

print(get_element(list1, 4))
print("Expected: 50")

print()

print(get_element(list2, 0))
print("Expected: a")

print()

print(get_element(list3, 5))
print("Expected: Out of bounds.")

