"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no
"""

number_on_the_ticket = int(input('What is number on your ticket? Enter it: '))
if number_on_the_ticket < 100000 or number_on_the_ticket > 999999:
    print('Oh, this is wrong ticket and it makes wrong honey! We can not define its luckyness!')
else:
    first_digit = number_on_the_ticket // 100000
    second_digit = (number_on_the_ticket - first_digit * 100000) // 10000
    third_digit = (number_on_the_ticket - first_digit * 100000 - second_digit * 10000) // 1000
    fourth_digit = (number_on_the_ticket - first_digit * 100000 - second_digit * 10000 - third_digit * 1000) // 100
    fifth_digit = (number_on_the_ticket - first_digit * 100000 - second_digit * 10000
                    - third_digit * 1000 - fourth_digit * 100) // 10
    sixth_digit = number_on_the_ticket % 10
    if first_digit + second_digit + third_digit == fourth_digit + fifth_digit + sixth_digit:
        print('Your ticket is lucky!')
    else:
        print('You\'ve got unlucky ticket, sorry.')
