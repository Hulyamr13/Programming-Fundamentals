orders = int(input())
total_price = 0

for _ in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue

    order_price = days * price_per_capsule * capsules_per_day
    total_price += order_price

    print(f'The price for the coffee is: ${order_price:.2f}')
print(f"Total: ${total_price:.2f}")