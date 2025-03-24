coord=input()
letter1=coord[0]
number1=int(coord[1])
letter2=coord[3]
number2=int(coord[4])
letter_1=ord(letter1)-ord('a')+1
letter_2=ord(letter2)-ord('a')+1
if (abs(letter_1-letter_2)==1 and
    abs(number1-number2)==2) or (abs(letter_1-letter_2)==2 and
                                                     number1-number2==1):
  print('верно')
else:
  print('ошибка')
