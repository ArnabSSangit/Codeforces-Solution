txt = input()
 
x = txt.split("WUB")
 
for i in range(0,len(x)):
    if x[i] !=None:
        print(x[i],end=' ')
