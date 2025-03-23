number= input()
n, k, m = map(int, number.split(' '))
time=0
while n>0:
    n-=k
    time+=m
print(2*time)
