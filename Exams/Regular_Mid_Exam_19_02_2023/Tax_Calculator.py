vehicles = input().split('>>')
total_tax = 0

for vehicle in vehicles:
    current_car = vehicle.split(' ')
    years = int(current_car[1])
    kilometers = int(current_car[2])
    if current_car[0] == "family":
        tax = 50
        for year in range(1, years + 1):
            tax -= 5
        while kilometers - 3000 >= 0:
            tax += 12
            kilometers -= 3000
        total_tax += tax
        print(f"A {current_car[0]} car will pay {tax:.2f} euros in taxes.")
    elif current_car[0] == "heavyDuty":
        tax = 80
        for year in range(1, years + 1):
            tax -= 8
        while kilometers - 9000 >= 0:
            tax += 14
            kilometers -= 9000
        total_tax += tax
        print(f"A {current_car[0]} car will pay {tax:.2f} euros in taxes.")
    elif current_car[0] == "sports":
        tax = 100
        for year in range(1, years + 1):
            tax -= 9
        while kilometers - 2000 >= 0:
            tax += 18
            kilometers -= 2000
        total_tax += tax
        print(f"A {current_car[0]} car will pay {tax:.2f} euros in taxes.")
    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")