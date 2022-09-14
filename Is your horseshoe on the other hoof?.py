s = list(map(int,input().split()))
sol=[]
for color in s:
    if color not in sol:
        sol.append(color)
 
print(4-len(sol))
