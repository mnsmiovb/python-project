examScore=int(input("Write your exam score:"))
schoolScore=int(input("Write your school score:"))
studentAge=int(input("Write your  age:"))
if studentAge<0:
    print('invalid age')
elif examScore<0:
    print('invalid score')
elif examScore>700:
    print('invalid score')
elif schoolScore<0:
     print('invalid score')
elif schoolScore>100:
    print('invalid score')
else:
    if studentAge>=16:
        if examScore<300:
            print('Sorry you are not accepted ,your exam score isnt enough')
        elif examScore<=449:
            if schoolScore>=80:
                print("Congratulations!!! You have been accepted to university. Reason: your school score is above 80")
            else:
                print('Sorry you are not accepted ,your school score isnt enough')
        elif examScore<=599:
            print("Congratulations!!! You have been accepted to university.Reason: your exam score is enough")
        else:
            print("Congratulations!!! You have been accepted to university.You get shcolarship.Reason: your exam score is enough")
    else:
        print('Sorry you are not accepted ,your age is under 16')