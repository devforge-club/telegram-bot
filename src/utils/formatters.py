
def int_to_roman(num: int) -> str:
  """Convierte entero a números romanos (hasta 3999)"""
  if num <= 0 or num > 3999:
      raise ValueError("Number must be between 1 and 3999")

  values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

  result = ""
  for value, symbol in zip(values, symbols):
      count = num // value
      result += symbol * count
      num -= value * count
  return result
