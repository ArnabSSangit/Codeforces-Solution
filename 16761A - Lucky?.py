t  = int(input())
for i in range(t):
    n = input()
    s1 = n[:3]
    s2 = n[3:]
    c1 = 0
    c2=0
    for i in range(len(s1)):
        c1 = c1+int(s1[i])
        c2 = c2+int(s2[i])

    if c1==c2:
        print("YES")
    else:
      print("NO")
