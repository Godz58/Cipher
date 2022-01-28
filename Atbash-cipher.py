plain_text = input("enter your text: ")
operation = int(input("choose 1 to encipher and 2 to decipher: "))

if operation == 1:

    for i in range (len(plain_text)):
        if plain_text[i] ==" ":
          print(" ",end = "")
          continue

        num = 122 - ord(plain_text[i])
        c =( ord(plain_text[i])+ num ) - (ord(plain_text[i]) - ord('a'))

        print(chr(c), end = "")

if operation == 2:

    for i in range(len(plain_text)):
        if plain_text[i] == " ":
            print(" ", end="")
            continue

        num = 97 - ord(plain_text[i])
        c = (ord(plain_text[i]) + num) - (ord(plain_text[i]) - ord('z'))

        print(chr(c), end="")