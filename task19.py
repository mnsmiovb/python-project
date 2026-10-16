drinkCode=input('What you want to drink.T-Tea,C-coffee,J-juice')
quantity=int(input('How many would you like?from 1 to 10'))
if quantity<1 or quantity>10:
        print('Invalid quantity')
else:
    match drinkCode:
       case 'T':
        price=2
        drink='tea'
       case 'C':
        price=4
        drink='coffee'
       case 'J':
        price=3
        drink='juice'
       case _:
        drink="none"
    if drink=="none":
        print(' unknown code')
    else:
      total=price*quantity
      orderSize='Large order' if total>=20 else 'Regular order'
      print('Drink is',drink,'.Quantity is',quantity,'.Then total price is',total,'and order is a',orderSize)