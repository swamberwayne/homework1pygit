#Wayne Swamber Jr
#1419882

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")

print()
#services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}

print("Select first service:")
first_service = input()
print("Select second service:")
second_service = input()
print()

print("Davy's auto shop invoice")
print()

total = 0

if first_service == "Oil change":
    print("Service 1: Oil change, $35")
    total = total + 35
elif first_service == "Tire rotation":
    print("Service 1: Tire rotation, $19")
    total = total + 19
elif first_service == "Car wash":
    print("Service 1: Car wash, $7")
    total = total + 7
elif first_service == "Car wax":
    print("Service 1: Car wax, $12")
    total = total + 12
elif first_service == "-":
    print("Service 1: No service")
    total = total + 0
else:
    print("No first service selected")

if second_service == "Oil change":
    print("Service 2: Oil change, $35")
    total = total + 35
elif second_service == "Tire rotation":
    print("Service 2: Tire rotation, $19")
    total = total + 19
elif second_service == "Car wash":
    print("Service 2: Car wash, $7")
    total = total + 7
elif second_service == "Car wax":
    print("Service 2: Car wax, $12")
    total = total + 12
elif second_service == "-":
    print("Service 2: No service")
    total = total + 0
else:
    print("No second service selected")

print()
print('Total: ${}'.format(total))