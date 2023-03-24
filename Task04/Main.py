"""
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом
по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
Пример:
3 2 4 -> yes
3 2 1 -> no
"""

length_of_choco = int(input('Enter length of chocolate: '))
width_of_choco = int(input('Enter width of chocolate: '))
size_of_piece = int(input('Enter size of chocolate squares on the broken piece: '))
if size_of_piece % length_of_choco == 0 or size_of_piece % width_of_choco == 0:
   print('Yeah, you can do it!')
else:
    print('Nope, you can\'t do it (if you are not a cheater).')