userAge=int(input('Write your age:'))
if userAge>=0:
    if userAge<=12:
        print("You are in child category")
    elif userAge<=17:
        print("You are in teenager category")
    elif userAge<=64:
         print("You are in adult category")
    else:
         print("You are in senior category")
else:
     print("Invalid age")