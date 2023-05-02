message = input('Insert your message here please')
new_message = ''
message = message.upper()

for char in message:
    length = len(new_message)+1
    if char != message[0]:
        if char.isalpha():
            if (ord(char)+key)>90:
                if (length%60==0):
                    new_message += '/n'
                    new_message += chr(ord(char)-key)
                elif (length%6!=0) :
                    new_message += chr(ord(char)-key)
                elif (length%6==0):
                    new_message += ' '
                    new_message += chr(ord(char)-key)
                    length -=1
            elif (ord(char)-key)<90:
                if (length%60==0):
                    new_message += '/n'
                    new_message += chr(ord(char)+key)
                elif (length%6!=0) :
                    new_message += chr(ord(char)+key)
                elif (length%6==0):
                    new_message += ' '
                    new_message += chr(ord(char)+key)

        else:
            continue
    else:
        if (ord(char)+key)>90:
            new_message += chr(ord(char)-key)
        else:
            new_message += chr(ord(char)+key)
print(new_message)
