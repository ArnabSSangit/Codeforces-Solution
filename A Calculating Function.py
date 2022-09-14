def letters(s):
    if s%2==0:
        print(int(s/2))
    else:
        print(int(-(s+1)/2))
 
 
 
if __name__ == "__main__":
    s = int(input())
    letters(s)
