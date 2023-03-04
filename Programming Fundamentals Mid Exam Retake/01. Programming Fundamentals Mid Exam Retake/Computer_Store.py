def calculate_receipt():
    prices_without_tax = []

    while True:
        price = input()

        if price == "special" or price == "regular":
            break

        try:
            price = float(price)
            if price <= 0:
                print("Invalid price!")
                continue
            prices_without_tax.append(price)
        except:
            print("Invalid price!")
            continue

    if len(prices_without_tax) == 0:
        print("Invalid order!")
        return

    total_price_without_tax = sum(prices_without_tax)
    total_tax_amount = 0.2 * total_price_without_tax
    total_price_with_tax = total_price_without_tax + total_tax_amount

    if price == "special":
        total_price_with_tax *= 0.9

    print("Congratulations you've just bought a new computer!")
    print("Price without taxes: {:.2f}$".format(total_price_without_tax))
    print("Taxes: {:.2f}$".format(total_tax_amount))
    print("-----------")
    print("Total price: {:.2f}$".format(total_price_with_tax))


calculate_receipt()
