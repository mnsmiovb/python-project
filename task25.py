studentID=input('Enter your ID: ')
studentAge=input('Enter your age: ')
workshopCode=input('Enter workshop code(PY,WEB,CY): ')
payment=input('Enter payment: ')
if len(studentID)!=8:
    print('ID must be 8 digits')
elif not studentID.isdecimal() or not studentID.isascii():
    print('Only ASCII digits')
elif len(studentAge)==0:
    print("Age is required")
elif not studentAge.isascii() or not studentAge.isdecimal():
    print('Only ASCII digits')
elif int(studentAge)<16 or int(studentAge)>65:
    print('Student age must be between 16 and 65')
else:
    studentAge=int(studentAge)
    match workshopCode:
        case 'PY':
            workshop='Python Basics'
            fee=30
            minAge=16
        case 'WEB':
            workshop='Web Development'
            fee=40
            minAge=16
        case 'CY':
            workshop='Cyber security'
            fee=50
            minAge=18
        case _:
            workshop='unknown'
            fee=0
            minAge=0
    if workshop=="unknown":
         print('Invalid workshop code')
    elif studentAge<minAge:
            print('Students age is under minimum age')
    else:
            discount=fee*0.2 if  16<=studentAge<=18 else 0
            finalFee=fee-discount
            if len(payment)==0:
              print('Pls Enter payment')
            elif not payment.isdecimal() or not payment.isascii():
              print('Only ASCII digits')
            else:
              payment=int(payment)
              if payment<finalFee:
                missing=finalFee-payment
                print('Insufficient payment','Missing amount is',missing,'AZN')
              else:
                change= payment-finalFee
                print("Registration confirmed")
                print('Student ID: ',studentID)
                print("Workshop: ",workshop)
                print('Discount: ',discount,'AZN')
                print("Final Fee: ",finalFee,'AZN')
                print('Change: ',change,'AZN') 
        