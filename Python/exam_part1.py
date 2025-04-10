# Joey Coladipietro

def repeat_start(s):
    """
    Given a string, return a new string where the first two characters 
    are repeated 
    three times. If the string is shorter than two characters, 
    return the string repeated three times.
    repeat_start("hello") returns "hehehe"
    repeat_start("a") returns "aaa"
    """
    if len(s) >= 2:
        return s[:2] * 3
    else:
        return s * 3


def shift_left(lst):
    """
    Given a list, rotate its elements to the left by one position. 
    The last element should become the first.
    shift_left([1, 2, 3, 4]) returns [2, 3, 4, 1]
    shift_left([5]) returns [5]
    """
    if len(lst) > 1:
        first_element = lst.pop(0)
        lst.append(first_element)
    return lst
    
    

    

def count_digits(s):
    """
    Use a comprehension to count the number of digits in a string.
    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    count_digits("The year is 2025!") returns 4
    The string function isdigit() returns True if the string is a digit.
    Eg. c='1' c.isdigit() returns True
    """
    digits = [1 for char in s if char.isdigit()]
    return sum(digits)

def swap(lst):
    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """
    min_index = 0
    first_element = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
    min_element = lst[min_index]
    lst[0] = min_element
    lst[min_index] = first_element
    
    return lst



def build_grades_dict():
    '''
    Create a dictionary where the key is a student's name and the value is
    their grade stored as an integer. 
    Read in the file, grades.txt, store the student's first and last name as 
    the key (first and last name should have a space between them) 
    and their grade as the integer value.
    Your output should read:
     {'Alice Brown': 90, 'Bob Smith': 85, 'Charlie Johnson': 78, 
     'Daisy Lee': 92, 'Evelyn Taylor': 88}
    '''
    grade_dict = {}
    with open("grades.txt", "r") as file:
        for line in file:
            info = line.strip().split()
            if info[0] != "Daisy":
                full_name = info[0] + " " + info[1]
                grade = int(info[2])
                grade_dict.update({full_name:grade})
            else:
                full_name1 = info[0] + " " + info[1]
                full_name2 = info[3] + " " + info[4]
                grade1 = int(info[2])
                grade2 = int(info[5])
                grade_dict.update({full_name1:grade1})
                grade_dict.update({full_name2:grade2})
        return grade_dict
            

            
# Test Cases
print('repeat_start("hello") expected: hehehe')
print('repeat_start("hello") actual:', repeat_start("hello"))
print('repeat_start("a") expected: aaa')
print('repeat_start("a") actual:', repeat_start("a"))
print('repeat_start("jo") expected: jojojo')
print('repeat_start("jo") actual:', repeat_start("jo"))
print()

print('shift_left([1, 2, 3, 4]) expected: [2, 3, 4, 1]')
print('shift_left([1, 2, 3, 4]) actual:', shift_left([1, 2, 3, 4]))
print('shift_left([6, 7, 8]) expected: [7, 8, 6]')
print('shift_left([6, 7, 8]) actual:', shift_left([6, 7, 8]))
print('shift_left([13, 14]) expected: [14, 13]')
print('shift_left([13, 14]) actual:', shift_left([13, 14]))
print()

print('count_digits("The year is 2025!") expected: 4')
print('count_digits("The year is 2025!") actual:', count_digits("The year is 2025!"))
print('count_digits("Villanova basketball has won 3 national championships.") expected: 1')
print('count_digits("Villanova basketball has won 3 national championships.") actual:', 
      count_digits("Villanova basketball has won 3 national championships."))
print('count_digits("#TB12") expected: 2')
print('count_digits("#TB12") actual:', 
      count_digits("#TB12"))

print()

print('swap([5,4,3,2,1]) expected: [1, 4, 3, 2, 5]')
print('swap([5,4,3,2,1]) actual:',swap([5,4,3,2,1]))
print('swap([2,2,2,1,2]) expected: [1, 2, 2, 2, 2]')
print('swap([2,2,2,1,2]) actual:',swap([2,2,2,1,2]))
print('swap([1,1,1,1,1]) expected: [1, 1, 1, 1, 1]')
print('swap([1,1,1,1,1]) actual:',swap([1,1,1,1,1]))
print()

print({'Alice Brown': 90, 'Bob Smith': 85, 'Charlie Johnson': 78, 
     'Daisy Lee': 92, 'Evelyn Taylor': 88})
print(build_grades_dict())
print()
