plain_text = input("enter your text: ")
key = input("enter your key: ")
operation =int( input("choose 1 to encrypt and 2 to decrypt: "))
j=0
for i in range(len(plain_text)):
    if plain_text[i] == " ":
        continue
    else:
        j=j+1
ind = 0
while(j>len(key)): #key's length equal the plain_text's length
    key= key + key[ind]
    ind = ind + 1
ck = 0
if operation == 1:
    for cp in range (len(plain_text)):
        if plain_text[cp] == " ":
            print(" ",end="")
            cp = cp + 1
        else:
            C = ((ord(plain_text[cp]) - ord("a")) + (ord(key[ck]) - ord("a"))) % 26
            print(chr(C + ord("a")), end="")
            ck = ck+1
if operation == 2:
    for cp in range (len(plain_text)):
        if plain_text[cp] == " ":
            print(" ",end="")
            cp = cp + 1
        else:
            C = ((ord(plain_text[cp]) - ord("a")) - (ord(key[ck]) - ord("a"))) % 26
            print(chr(C + ord("a")), end="")
            ck = ck+1