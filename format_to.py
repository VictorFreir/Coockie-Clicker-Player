def to_float(number):
    if ',' in number:
        number = number.replace(',','')
    number = float(number)

    return number