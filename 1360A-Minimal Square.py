t  = int(input())
for i in range(t):
    a,b =map(int,input().split())
    side  = min(max(a*2,b),max(b*2,a))
    print(side*side)

