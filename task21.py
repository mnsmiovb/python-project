pin='0427'
pinAttempt=input('Enter your pin')
if len(pinAttempt)==0:
    print("PIN is required")
elif len(pinAttempt)!=4:
    print("Wrong length") 
elif not pinAttempt.isascii() or not pinAttempt.isdecimal():
    print("Digits only")
elif pin==pinAttempt:
    print("Access granted")
else:
    print("Incorrect PIN")