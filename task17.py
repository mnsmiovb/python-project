orderTotal=int(input('Write a non-negative order total in AZN:'))
membershipAnswer=input("Do you want to be our member?")
if orderTotal<0 or (membershipAnswer!="yes" and membershipAnswer!="no"):
    print('Invalid process')
else:
    deliveryFee=0 if orderTotal>=50 or membershipAnswer=='yes' else 5
    finalTotal=orderTotal+deliveryFee
    print('Delivery fee is',deliveryFee,'AZN .Final total is',finalTotal,'AZN.')
    