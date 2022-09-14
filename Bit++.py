c=0
t=int(input())
for i in range(0,t):
    x = input()
    if x[0] =="+" or x[1]=="+":
        c=c+1
 
    else:
        c=c-1
 
 
print(c)
