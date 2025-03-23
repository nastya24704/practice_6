square = input()
k = int(input())
m, n = map(int, square.split('*'))
if k%m == 0 or k%n==0:
    print('успешно')
else:
    print('неосуществимо')
