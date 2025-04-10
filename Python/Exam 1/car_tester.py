from cars import Car

car_list = []
with open("cars.txt", "r") as file:
    for line in file:
        info = line.strip().split()
        car = Car(info[0], info[1], int(info[2]), int(info[3]))
        car_list.append(car)

print(str(car_list[0]))
print(str(car_list[1]))
    