#####-----Convert UpperCase String to LowerCase String.-----#####


word = input("Enter UpperCase String: ")
def split(word):
    return list(word)
s = split(word)


x = ""
for i in range(0,len(s)):
    ch = ord(s[i])
    a = ch+32
    up = chr(a)
    x= x+up

a = x.replace("@"," ")
print("LowerCase String: " +a)

print("Given String Length is: " + str(len(s)))


####### @eswarkada
