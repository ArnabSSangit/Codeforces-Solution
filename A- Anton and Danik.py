n = int(input())
s = input()
anton = 0
danik = 0
 
for i in range(0,n):
    if s[i] == "A":
        anton = anton+1
 
    elif s[i]== "D":
        danik = danik+1
 
    i=i+1
 
 
 
if anton==danik:
    print("Friendship")
 
if anton>danik:
    print("Anton")
 
elif danik>anton:
    print("Danik")
