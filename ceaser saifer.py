text="hello,world 2026 !"
sift=4
mood="encrypt"#change to "decrypt"to reverse it
if mood=="decrypt":
    shift=-shift
result=""
for char in text:
    if char.isupper():
     result +=chr((ord(char)+shift-65)%26+65)
    elif char.islower():
          result +=chr((ord(char)+shift-97)%26+97)
          #check for digits 0-9
    elif char.isdigit():
          #subtract 48(ASCII for '0')and wrap around using modulo 10
          result +=chr((ord(char)+shift-48)%10+48)
    else:
          result +=char
print(f"result ({mode}ed): {result}")