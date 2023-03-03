def get_even_add_odd_sum(digits_as_str):
    even_sum = 0
    odd_sum = 0

    for digit_as_str in digits_as_str:
        digit = int(digit_as_str)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


nums_as_str = input()
print(get_even_add_odd_sum(nums_as_str))