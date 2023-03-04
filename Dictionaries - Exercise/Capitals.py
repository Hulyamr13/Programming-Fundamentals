countries = input().split(", ")
capitals = input().split(", ")

capital_country = {countries[idx]: capitals[idx] for idx in range(len(countries))}
for country, capital in capital_country.items():
    print(f"{country} -> {capital}")