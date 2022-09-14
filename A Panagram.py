def panagram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s.lower():
            return False
 
    return True
 
 
if __name__ == "__main__":
    n =  int(input())
    s = input()
    if panagram(s)==True:
        print("YES")
 
    else:
        print("NO")
