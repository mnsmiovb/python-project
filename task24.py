productCode=input('Write product code.(K,M,H): ')
quantity=input('Write quantity(from 1 to 5): ')
couponCode=input('Write coupon code (SAVE10 or NONE): ')
deliveryCode=input('Write delivery code (Pickup or standart): ')
if len(quantity)==0:
    print('Pls enter quantity')
elif not quantity.isascii() or not quantity.isdecimal():
    print('Only ASCII digits')
elif int(quantity)<1 or int(quantity)>5:
    print('Quantity must be between 1 and 5')
else:
    match productCode:
        case 'K':
            price=40
            product='Keyboard'
        case 'M':
            price=20
            product='Mouse'
        case "H":
            price=60
            product='Headphones'
        case _:
            product='unknown'
    if product=='unknown':
        print('Invalid product')
    else:
        quantity=int(quantity)
        subtotal=quantity*price
        if couponCode=='NONE':
            discount=1
            discountAmount=0    
        elif couponCode=='SAVE10':
            if subtotal>=100:
                discount=0.1
                discountAmount=subtotal*discount
            else:
                discount=1
                discountAmount=0
        else:
            print('Invalid coupon code') 
        
        match deliveryCode:
            case 'P':
                fee=0
            case 'S':
                fee=0 if subtotal-discountAmount>=80 else 5
            case _:
                fee='unknown'
        if fee=='unknown':
                print('Delivery code is invalid')
        else:
                print('Product is',product) 
                print('Quantity is',quantity)
                print("Subtotal is",subtotal)
                print("Discount amount is",discountAmount)
                print('Delivery fee is',fee)
                print('.Then final total is equal',subtotal-discountAmount+fee)