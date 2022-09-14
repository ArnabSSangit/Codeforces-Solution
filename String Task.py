vowel = ['a','o','y','e','u','i']
s = ''
string = str(input())
k = string.lower()
for a in range(len(string)):
    if k[a] not in vowel:
        s+='.'
        s+=k[a]
 
print(s)
