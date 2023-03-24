"""
Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

number = int(input('Enter a three-digit number: '))
hundreds = number // 100
tens = (number - hundreds*100) // 10
units = number % 10
print(hundreds, tens, units)
print(f'Sum of digits of {number} is {hundreds+tens+units}.')