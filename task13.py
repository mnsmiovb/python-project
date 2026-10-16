userAge=int(input('Write your age:'))
monthlySalary=int(input("Write your monthly salary:"))
requestedLoanAmount=int(input("Write requested loan amount:"))
if userAge<0:
    print('Invalid age')
elif  monthlySalary<0:
    print('Invalid salary')
elif requestedLoanAmount<=0:
    print('Invalid amount')
else:
    if userAge>=18:
        if monthlySalary>=500:
            if requestedLoanAmount<monthlySalary*10:
                print("Congratulations your loan approved.Reason:All conditions are satisfied")
            else:
                print('Soryy yout loan rejected.Reason:Requested loan is above 10 times the salary')
        else:
            print("Sorry yout loan rejected.Reason: User's salary is under 500")
    else:
        print("Sorry yout loan rejected.Reason: User's age  is under 18")