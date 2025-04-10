name = input("Enter your name.")
print("Hello, ", name)

try:
    num = int(input("Enter a number."))
    print("You entered", num)
    double = num * 2
    print("Doubled", double)
except:
    print("Not a number.")

with open("movies.txt") as file:
    for line in file:
        print(line.strip())
    
with open("heights.txt") as file:
    for line in file:
        info = line.strip().split()
        info[2] = int(info[2])
        print(info)

# 1. Prompt user to enter a filename
# 2. Open file and print each line with the line number

file_name = input("Enter the file name.")
with open(file_name) as file:
    count = 1
    for line in file:
        print(str(count) + ". " + line.strip())
        count += 1
