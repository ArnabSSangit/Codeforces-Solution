word = input()
 
lower = 0
upper = 0
 
for char in word:
    if char.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    word = word.upper()
else:
    word = word.lower()
 
print(word)
