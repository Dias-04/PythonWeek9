def convert_to_base(num, base):
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while num > 0:
        result = digits[num % base] + result
        num //= base
    return result or "0"

number = 25
base = 16
print(f"{number} in base {base} is: {convert_to_base(number, base)}")
