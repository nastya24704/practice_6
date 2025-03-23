window = input()
fortress = input()
a, b = map(int, window.split('*'))
c, d, e = map(int, fortress.split('*'))
if a*b>= c*d or a*b>= c*e or a*b>= e*d:
    print('да')
else:
    print('нет')
