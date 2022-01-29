while(True):
    print("please choose one of the following: ")
    print("1) to encipher in R0T_13 (caeser cipher)")
    print("2) to encipher in Atbash cipher")
    print("3) to encipher in XOR cipher")
    print("4) to encipher in Vigenere cipher)")
    oper = int(input())
    if oper == 1:
        print("enter your messege ")
        msg = input()
        rot_num = int(input("ROT number?: "))
        operation = input("encrypt or decrypt?: ")
        if operation == 'encrypt':
            for i in range(len(msg)):
                if msg[i] == " ":
                    print(" ", end="")
                    continue
                if ord(msg[i]) + rot_num > 122:
                    enc_msg = ord('a') + (ord(msg[i]) + rot_num - 123)
                    print(chr(enc_msg), end="")
                else:
                    enc_msg = ord(msg[i]) + rot_num
                    print(chr(enc_msg), end="")
        if operation == 'decrypt':
            print("warning: your message will be encrypted if it is already decrypted.")
            for i in range(len(msg)):
                if msg[i] == " ":
                    print(" ", end="")
                    continue
                if ord(msg[i]) - rot_num < 97:
                    enc_msg = ord('z') - (122 - ord(msg[i]) - rot_num)
                    print(chr(enc_msg), end="")
                else:
                    enc_msg = ord(msg[i]) - rot_num
                    print(chr(enc_msg), end="")
        break

    if oper == 2:
        plain_text = input("enter your text: ")
        operation = int(input("choose 1 to encipher and 2 to decipher: "))

        if operation == 1:

            for i in range(len(plain_text)):
                if plain_text[i] == " ":
                    print(" ", end="")
                    continue

                num = 122 - ord(plain_text[i])
                c = (ord(plain_text[i]) + num) - (ord(plain_text[i]) - ord('a'))

                print(chr(c), end="")

        if operation == 2:

            for i in range(len(plain_text)):
                if plain_text[i] == " ":
                    print(" ", end="")
                    continue

                num = 97 - ord(plain_text[i])
                c = (ord(plain_text[i]) + num) - (ord(plain_text[i]) - ord('z'))

                print(chr(c), end="")
        break

    if oper == 3:
        plain_text = input("Enter your text: ")
        key = input("Enter your key: ")


        def encrypt(plain_text, key):
            ck = 0
            encrypted = []
            encipherd = ['0x']
            for ct in range(len(plain_text)):
                if plain_text[ct] == " ":
                    print(" ", end="")
                    continue
                else:
                    encrypted.append(ord(plain_text[ct]) ^ ord(key[ck]))
                    ck += 1
                    enc_splited = hex(encrypted[ct]).split("0x")
                    encipherd.append(enc_splited[1])
                    if len(plain_text) - 1 > ct:
                        encipherd.append("-")
            for q in range(len(encipherd)):
                print(encipherd[q], end="")


        j = 0
        for i in range(len(plain_text)):
            if plain_text[i] == " ":
                continue
            else:
                j = j + 1
        ind = 0
        while (j > len(key)):  # key's length equal the plain_text's length
            key = key + key[ind]
            ind = ind + 1
        encrypt(plain_text, key)
        break

    if oper == 4:
        plain_text = input("enter your text: ")
        key = input("enter your key: ")
        operation = int(input("choose 1 to encrypt and 2 to decrypt: "))
        j = 0
        for i in range(len(plain_text)):
            if plain_text[i] == " ":
                continue
            else:
                j = j + 1
        ind = 0
        while (j > len(key)):  # key's length equal the plain_text's length
            key = key + key[ind]
            ind = ind + 1
        ck = 0
        if operation == 1:
            for cp in range(len(plain_text)):
                if plain_text[cp] == " ":
                    print(" ", end="")
                    cp = cp + 1
                else:
                    C = ((ord(plain_text[cp]) - ord("a")) + (ord(key[ck]) - ord("a"))) % 26
                    print(chr(C + ord("a")), end="")
                    ck = ck + 1
        if operation == 2:
            for cp in range(len(plain_text)):
                if plain_text[cp] == " ":
                    print(" ", end="")
                    cp = cp + 1
                else:
                    C = ((ord(plain_text[cp]) - ord("a")) - (ord(key[ck]) - ord("a"))) % 26
                    print(chr(C + ord("a")), end="")
                    ck = ck + 1
        break
    else:
        print("please enter a valid option")
        continue