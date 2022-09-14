t = int(input())
for i in range(0,t):
    s=int(input())
    if s>=1900:
        print("Division 1")
    elif s>=1600 and s<=1899:
        print("Division 2")
    elif s>=1400 and s<=1599:
        print("Division 3")
    elif s<=1399:
        print("Division 4")
