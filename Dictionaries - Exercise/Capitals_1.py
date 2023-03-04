countries = input().split(", ")
capitals = input().split(", ")

capital_by_country = {}
for idx in range(len(countries)):
    country = countries[idx]
    capital = capitals[idx]
    capital_by_country[country] = capital
    print(f'{country} -> {capital}')