def zero(s):
    one=0
    zero=0
 
    for i in range(0,len(s)):
        if s[i]=="0":
            zero=zero+1
        elif s[i]=="1":
            one=one+1
 
 
    print(abs(one-zero))
 
 
if __name__ == "__main__":
    n= int(input())
    s= input()
    zero(s)
