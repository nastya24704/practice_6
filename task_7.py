number= int(input())
while number>0:
    number -=7
    if number%5==0:
        while number>0:
            number-=5
if number ==0:
    print('да')
else:
    print('нет')
