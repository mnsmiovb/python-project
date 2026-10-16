amount=float(input('Write purchase amount in AZN:'))
if amount>=0:
    if amount<100:
        print('The original price is',amount,'and no discount.So final price is',amount)
    elif amount<300:
        discountUnder300=10/100
        print('The original price is',amount,'and discount is',discountUnder300*100,'% .So final price is',amount*(1-discountUnder300))
    elif amount<500:
        discountUnder500=15/100
        print('The original price is',amount,'and discount is',discountUnder500*100,'% .So final price is',amount*(1-discountUnder500))
    else:
        discountMore500=20/100
        print('The original price is',amount,'and discount is',discountMore500*100,'% .So final price is',amount*(1-discountMore500))
else:
    print('Invalid amount')