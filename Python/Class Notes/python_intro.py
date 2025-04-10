print("Hello World!")

# this is single line with a comment

'''
multiple lines of comments
line 2
'''

# highlight + command + / to comment out entire rows
# line 1
# line 2
# line 3

# Variables
x = 10
x = "hello"
x = [1, 2, 3]
print(x)

x = 100
y = 10
result = int(x / y)
result = int(result)
print(result)

# "//" will divide and take the floor of number
x = 105
result = x // y
print(result)

# minimum / maximum
min_val = min(1, 10, 50)
print(min_val)
raised = pow(2, 3) # 2 to the power of 3 (2^3)
print(raised)
raised = 2**3
print(raised)

# if else statements
x = -1
y = 0
if x < 0:
    print("x is negative")
    #x = 10
elif x > 0:
    print("x is positive")
else:
    print("x is 0")

# compound conditional statements
start = 10
end = 100

if x >= start and x <= end:
    print("x is within range")

if x < start or x > end:
    print("x is not within of range")

# while loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# for loop
# range(start, end - 1, increment)
for i in range(1, 7, 1):
    print(i, end = " ")
print()

lst = [2, 4, 6, 8]

for i in range(len(lst)):
    print(i, lst[i], end = " ")
print()

for val in lst:
    print(val)

for i, val, in enumerate(lst):
    print(i, val, end = " ")

print()
'''
Exercise 1: Printing Numbers
Write a for loop to print all numbers from 1 to 20 that are divisible by 3.
'''
for i in range(1, 21):
    if i % 3 == 0:
        print(i, end = " ")

print()
'''
Exercise 2: Sum of Even Numbers
Write a while loop that calculates the sum of all even numbers between 1 and 50 (inclusive). Print the
result.
'''
counter = 1
sum = 0
while counter <= 50:
    if counter % 2 == 0:
        sum += counter
    counter += 1
print(sum)

print()
'''
Exercise 3: List Manipulation
You are given a list of numbers:
numbers = [5, 8, 2, 15, 10, 3, 7]
1. Use a for loop to print the numbers greater than 5
'''
numbers = [5, 8, 2, 15, 10, 3, 7]
for val in numbers:
    if val > 5:
        print(val, end = " ")

print()
lst = [1, 2, 3, 4, 5]
lst2 = []

for i, val in enumerate(lst):
    if i == 0:
        lst2.append(lst[0])
    else:
        lst2.append(lst[i] + lst2[i - 1])

print(lst2)

# Functions

def hello_world():
    print("Hello World!")
hello_world()

def hello(name):
    print("hello " + name)
    print("Hello", name)
hello("Bob")

def hello2(name = "Bob"):
    print("Hello " + name)
hello2()

'''
Exercise 1: Swap elements
Write a function called swap that takes a list of elements and swaps the first and last elements. For
example, if the input to the function is [0,3,8,4,5] the swapped list would be [5,3,8,4,0]. You do not need
to return the list. Test the function like this:
lst=[0,3,8,4,5]
swap(lst)
print(lst)
Test your function with another list to confirm it works on all input.
'''

def swap(list):
    list_beg = list[0]
    list_end = list[len(list) - 1]
    list[0] = list_end
    list[len(list) - 1] = list_beg

lst=[0,3,8,4,5]
swap(lst)
print(lst)

hello = "hello"
for c in hello:
    print(c)

course = "Platform Computing"
plat = course[:8]
comp = course[9:]
print(plat)
print(comp)