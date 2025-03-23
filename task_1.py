# диагональ прямоугольника: c = sqrt(a**2+b**2)
import math
rug = input()
a, b = map(int, rug.split('*'))
if math.sqrt(a**2+b**2) <= 2*6.5:
    print('да')
else:
    print('нет')
