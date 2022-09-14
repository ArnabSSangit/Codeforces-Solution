n , h = map(int, input().split())
a = list(map(int,input().split()))
sum = 0
for i in range(0,len(a)):
    if a[i]>h:
        sum=sum+2
 
    else:
        sum=sum+1
 
    i=i+1
 
 
print(sum)
