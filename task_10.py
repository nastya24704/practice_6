import turtle as trtl
coord_first = input()
x1, y1, x2, y2 = map(float, coord_first.split(' '))
coord_second = input()
a1, b1, a2, b2 = map(float, coord_second.split(' '))
# пусть перый прямоугольник abcd, тогда второй mnsk
length_1 = abs(x1-x2)
width_1 = abs(y1-y2)
length_2 = abs(a1-a2)
width_2 = abs(b1-b2)
trtl.up()
trtl.goto(x1, y1)
trtl.down()
for i in range(2):
    trtl.forward(length_1)
    trtl.right(90)
    trtl.forward(width_1)
    trtl.right(90)
trtl.up()
trtl.goto(a1, b1)
trtl.down()
for р in range(2):
    trtl.forward(length_2)
    trtl.right(90)
    trtl.forward(width_2)
    trtl.right(90)
if x2<a1 or a2<x1 or y1 < b2 or y2 > b1:
    print('Прямоугольники лежат вне друг друга, не касаясь.')
elif x1<a1 and x2>a2 and y1>b1 and y2<b2:
    print('Один прямоугольник лежит внутри другого,  не касаясь.')
elif a1 < x1 and a2 > x2 and b1 > y1 and b2 < y2:
    print('Один прямоугольник лежит внутри другого,  не касаясь.')
# это всегда только внешнее касание
elif x2==a1 or y1==b2 or y2==b1 or a2==x1:
    print('Прямоугольники имеют касание')
# внутреннее касание с хотя бы одной стороной, проверяем для каждой стороны
elif x1==a1 and y1>=a1 and y2<=a2 and x2>=a2:
    print('Прямоугольники имеют касание')
elif x1<=a1 and y1==a1 and y2<=a2 and x2>=a2:
    print('Прямоугольники имеют касание')
elif x1<=a1 and y1>=a1 and y2==a2 and x2>=a2:
    print('Прямоугольники имеют касание')
elif x1<=a1 and y1>=a1 and y2<=a2 and x2==a2:
    print('Прямоугольники имеют касание')
else:
    print('Прямоугольники имеют пересечение')
trtl.done()
