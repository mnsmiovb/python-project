studentScore=int(input('Write your score:'))
if studentScore>=0:
    if studentScore<=100:
        if studentScore<=50:
            print("Your score is F")
        elif studentScore<=60:
            print("Your score is E")
        elif studentScore<=70:
            print("Your score is D")
        elif studentScore<=80:
            print("Your score is C")
        elif studentScore<=90:
            print("Your score is B")
        else:
            print("Your score is A")
    else:
        print('Invalid Score')
else:
    print('Invalid Score')