pin='0427'
balance=1000
pinAttempt=input('Enter your pin: ')
amount=input('Write withdrawal amount: ')
if len(pinAttempt)!=4:
    print('Pin must be 4 digits')
elif not pinAttempt.isascii() or not pinAttempt.isdecimal():
    print('Only ASCII digits')
elif pin!=pinAttempt:
    print('Wrong pin')
else: 
    if len(amount)==0:
        print('Pls enter withdrawal amount')
    elif not amount.isdecimal() or not amount.isascii():
        print('Only ASCII digits')
    elif int(amount)<10 or int(amount)>500:
        print('The amount must be between 10 and 500 AZN')
    elif int(amount)%10!=0:
        print('The amount must be divisible by 10')
    else:
        amount=int(amount)
        fee=0 if amount>=200 else 2
        if amount+fee<=balance:
            print('Withdrawal balanca is',amount,"AZN.Fee is ",fee,"AZN. Then new balance is",balance-(amount-fee),"AZN.")