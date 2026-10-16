a=int(input('Write side lengh of triangle:'))
b=int(input("Write side lengh of triangle:"))
c=int(input("Write side lengh of triangle:"))
if a<=0:
    print('Invalid lengh')
elif b<=0:
    print('Invalid lengh')
elif c<=0:
    print('Invalid lengh')
else:
    if  a + b > c:
        if a + c > b:
            if b + c > a:
                if a==b==c:
                    print("Triangle is Equilateral")
                elif a==b or b==c or c==a:
                    print('Triangle is Isosceles')
                else:
                    print('Triangle is Scalene')
            else:
                print("Triangle cannot be created")
        else:
            print("Triangle cannot be created")
    else:
        print("Triangle cannot be created")