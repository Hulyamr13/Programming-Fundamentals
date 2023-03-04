def add_car_to_garage(garage, car, mileage, fuel):
    garage[car] = {int(mileage): int(fuel)}
    return garage


def drive_car(garage, car, distance, fuel):
    current_car_mileage, current_car_fuel = max(garage[car].items())
    if current_car_fuel < fuel:
        print("Not enough fuel to make that ride")
    elif current_car_fuel >= fuel:
        new_mileage = current_car_mileage + distance
        new_fuel = current_car_fuel - fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if new_mileage >= 100000:
            del garage[car]
            print(f"Time to sell the {car}!")
        else:
            garage[car] = {new_mileage: new_fuel}
    return garage


def refuel_car(garage, car, fuel):
    current_car_mileage, current_car_fuel = max(garage[car].items())
    if garage[car][current_car_mileage] + fuel > 75:
        refueled = 75 - garage[car][current_car_mileage]
        garage[car][current_car_mileage] = 75
    else:
        garage[car][current_car_mileage] += fuel
        refueled = fuel
    print(f"{car} refueled with {refueled} liters")
    return garage


def revert_car(garage, car, kilometers):
    current_car_mileage, current_car_fuel = max(garage[car].items())
    current_car_mileage -= kilometers
    if current_car_mileage < 10000:
        current_car_mileage = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    garage[car] = {current_car_mileage: current_car_fuel}
    return garage


def print_garage(garage):
    for car, mileage_and_fuel in garage.items():
        value = mileage_and_fuel
        key = value.keys()
        for mil in key:
            mileage = mil
        fuel = garage[car][mileage]
        print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")


number_of_cars = int(input())
garage = {}

for cars in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    garage = add_car_to_garage(garage, car, mileage, fuel)

command = input()
while command != "Stop":
    usage = command.split(" : ")
    current_usage = usage[0]
    car = usage[1]

    if current_usage == "Drive":
        distance = int(usage[2])
        fuel = int(usage[3])
        garage = drive_car(garage, car, distance, fuel)
    elif current_usage == "Refuel":
        fuel = int(usage[2])
        garage = refuel_car(garage, car, fuel)
    elif current_usage == "Revert":
        kilometers = int(usage[2])
        garage = revert_car(garage, car, kilometers)

    command = input()

print_garage(garage)