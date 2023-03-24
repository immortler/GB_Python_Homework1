"""
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше
журавликов, чем Петя и Сережа вместе?
Пример:
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
"""

number_of_cranes = int(input('Enter full number of paper cranes: '))
if number_of_cranes % 6 != 0:
    print('Somebody is lying or counted them wrong.')
else:
    print(f'Katya made {int(number_of_cranes - number_of_cranes/3)} cranes, '
    f'Petya and Seryozha made {int(number_of_cranes/6)} cranes everybody.')
