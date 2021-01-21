UserInput = ""
Cipher_Mode = ""
ShiftKey = 0
eMessage = ""

while (Cipher_Mode != "E" and Cipher_Mode != "D"):
    Cipher_Mode = input("E or D? : ")


if(Cipher_Mode == "E"):
    
    UserInput = input ("Provide message to Encrypt : ")
    ShiftKey = int(input ("Provide Shift Key value : "))
    UserInput = UserInput.upper()

    if (ShiftKey > 26):
        ShiftKey = ShiftKey % 26

    for element in UserInput:
        if(element.isalpha()):
            if( ord(element) + ShiftKey > 90):
                eMessage += chr(((ord(element)) - 26) + ShiftKey)
            else:
                eMessage += chr(ord(element) + ShiftKey)
        else:
            eMessage += element
        
    print(eMessage)  

else:
    UserInput = input ("Provide message to Decrypt : ")
    ShiftKey = int(input ("Provide Shift Key value : "))

    if(ShiftKey > 26):
        ShiftKey = ShiftKey % 26

    for element in UserInput:
        if(element.isalpha()):
            if( ord(element) - ShiftKey < 65):
                eMessage += chr(((ord(element)) - ShiftKey) + 26)
            else:
                eMessage += chr(ord(element) - ShiftKey)
        else:
            eMessage += element
        
    print(eMessage)
