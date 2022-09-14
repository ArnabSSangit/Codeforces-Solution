n =  int(input())
s  = input()
c=0
for i in range(0,n-1):
    if s[i]==s[i+1]:
        c=c+1
 
print(c)
