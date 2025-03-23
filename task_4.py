coord = input()
letter = coord[0]
number = int(coord[1])
if letter == 'a' or letter == 'c' or letter == 'e' or letter == 'g':
    if number % 2 != 0:
        print('черный')
    else:
        print('белый')
else:
    if number % 2 == 0:
        print('черный')
    else:
        print('белый')
