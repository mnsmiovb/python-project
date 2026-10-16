number1=float(input("write any number1:"))
number2=float(input("write any number2:"))
operation=input('Write one operation(+,-,*,/,%,**,//)')
checkingInteger=int(number2)
match operation:
    case "+":
        print("result",number1+number2)
    case "-":
         print("result",number1-number2)
    case "*":
        print("result",number1*number2)
    case "/":
        if number2==0:
            print('Invalid Operation')
        else:
            print("result",number1/number2)
    case "//":
        if number2==0:
             print('Invalid Operation')
        else:
             print("result",number1//number2)
    case "%":
         if number2==0:
            print('Invalid Operation')
         else:
             print("result",number1%number2)
    case "**":
        if number1==0 and number2<0:
            print('Invalid operation')
        elif number1<0 and number2!=checkingInteger:
             print('Invalid operation')
        else:
            print("result",number1**number2)
    case _:
        print('Invalid operation')

             