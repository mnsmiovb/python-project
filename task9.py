number1=int(input("write any number1:"))
number2=int(input("write any number2:"))
number3=int(input("write any number3:"))
if number1!=number2!=number3:
    if number1>number2 and number1>number3:
        if number2>number3:
            print('From smallest to largest',number3,number2,number1)
        else:
              print('From smallest to largest',number2,number3,number1)
    elif number2>number1 and number2>number3:
        if number1>number3:
            print('From smallest to largest',number3,number1,number2)
        else:
            print('From smallest to largest',number1,number3,number2)
    else:
        if number1>number2:
            print('From smallest to largest',number2,number1,number3)
        else:
            print('From smallest to largest',number1,number3,number3)
else:
    print("Dont agreed")