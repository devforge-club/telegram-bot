_ROMAN_MAPPING = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def int_to_roman(num: int) -> str:
    """Convierte entero a números romanos (hasta 3999)"""
    if num <= 0 or num > 3999:
        raise ValueError("Number must be between 1 and 3999")

    result = ""
    for value, symbol in _ROMAN_MAPPING:
        count = num // value
        result += symbol * count
        num -= value * count
    return result