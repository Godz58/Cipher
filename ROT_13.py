print("enter your messege ")
msg = input()
rot_num = int(input("ROT number?: "))
operation = input("encrypt or decrypt?: ")
if operation == 'encrypt':
    for i in range(len(msg)):
     if msg[i] == " ":
          print(" ", end="")
          continue
     if ord(msg[i])+rot_num > 122:
           enc_msg = ord('a')+(ord(msg[i])+rot_num - 123)
           print(chr(enc_msg), end="")
     else:
        enc_msg = ord(msg[i])+rot_num
        print(chr(enc_msg), end="")
if operation == 'decrypt':
    print("warning: your message will be encrypted if it is already decrypted.")
    for i in range(len(msg)):
     if msg[i] == " ":
          print(" ", end="")
          continue
     if ord(msg[i])-rot_num < 97:
           enc_msg = ord('z')-(122 - ord(msg[i])-rot_num)
           print(chr(enc_msg), end="")
     else:
        enc_msg = ord(msg[i])-rot_num
        print(chr(enc_msg), end="")
