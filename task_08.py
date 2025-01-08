def multiply_numbers(inputs = None):
    if not isinstance(inputs, str):
        inputs = str(inputs)

    val = 1

    for char in inputs:
        if char.isdigit():
            val *= int(char)

    if val != 1:
        return val
    else:
        return None

print(multiply_numbers('ss'))  # None
print(multiply_numbers())  # None
print(multiply_numbers('1234'))  # 24
print(multiply_numbers('sssdd34'))  # 12
print(multiply_numbers(2.3))  # 6
print(multiply_numbers([5, 6, 4]))  # 120

