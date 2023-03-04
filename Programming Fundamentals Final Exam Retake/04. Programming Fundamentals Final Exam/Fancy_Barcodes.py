import re


def validate_barcode(barcode):
    pattern = r"(@[#]+)([A-Z]([a-zA-Z0-9]{4,})[A-Z])(@[#]+)"
    digits_group = r"(\d+)"
    digits_product_group = '00'
    fancy_barcode = re.findall(pattern, barcode)
    if fancy_barcode:
        numbers_in_barcode = fancy_barcode[0][1]
        product_group = re.findall(digits_group, numbers_in_barcode)
        if product_group:
            digits_product_group = ''.join(product_group)
        return f"Product group: {digits_product_group}"
    else:
        return "Invalid barcode"


number_barcodes = int(input())

for barcodes in range(number_barcodes):
    barcode = input()
    print(validate_barcode(barcode))