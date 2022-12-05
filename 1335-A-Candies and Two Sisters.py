import math
n = int(input())

for i in range(0,n):
    i = int(input())
    if i ==2 or i ==1 :
        print("0")
    else:
        print(math.floor((i-1)/2))


