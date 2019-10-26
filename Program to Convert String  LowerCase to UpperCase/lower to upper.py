#########---- Convert LowerCase String to UpperCase String.----#########


word= input("Enter LowerCase String: ")
def split(word):
    return list(word)
s = split(word)
#print(s)

x=""
for i in range(0,len(s)):
    ch = ord(s[i])
    
  
    a = ch-32
    up = chr(a)
    x = x+up
    

print("UpperCase String: " + x)

print("given srting length is :" + str(len(s)))



######## @eswarkada




    
    


















'''for i in range(65,91):
    a = chr(i)
    print(a)'''
