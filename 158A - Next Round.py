n,k = map(int,input().split())
L = list(map(int,input().split()))
temp = L[k-1]
c= 0
for i in range(0,len(L)):
    if L[i]>0 and L[i]>=temp:
        c=c+1
print(c)
