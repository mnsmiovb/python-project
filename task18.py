dayNumber=int(input('Enter day number. 1 = Monday through 7 = Sunday:'))
match dayNumber:
    case 1:
        print('Its Monday- Study day')
    case 2:
        print('Its Tuesday- Study day')
    case 3:
        print('Its Wednesday- Study day')
    case 4:
        print('Its Thursday- Study day')
    case 5:
        print('Its Friday- Study day')
    case 6:
        print('Its Saturday- Weekend')
    case 7:
        print('Its Sunday- Weekend')
    case _:
        print('Invalid day')