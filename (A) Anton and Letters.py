def letters(s):
    unique = []
    for char in s [::]:
        if char !='{' and char !='}' and char !=',' and char !=' ':
            if char not in unique:
                unique.append(char)
 
    print(len(unique))
 
 
if __name__ == "__main__":
    s = input()
    letters(s)
