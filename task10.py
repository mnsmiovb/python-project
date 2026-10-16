withdrawalAmount=int(input('Write amount:'))
accountBalance=1000
if withdrawalAmount>0:
    if withdrawalAmount<=1000:
        print('Amount is',withdrawalAmount,'and reaminig balance is',accountBalance-withdrawalAmount)
    else:
        print('Unsufficient balance')
else:
    print('Inavlid balance')