phoneNumber=input('enter your phone number in the local format 0XXXXXXXXX: ')
if len(phoneNumber)==0:
    print('You didnt enter your phone number')
elif len(phoneNumber)!=10:
    print('Phone number must be 10 digits')
elif not phoneNumber.isdecimal() or not phoneNumber.isascii():
    print('Only digits')
else:
    prefixe=phoneNumber[0:3]
    match prefixe:
     case '050':
      company='azercell'
     case '051':
        company='azercell'
     case '055':
        company='bakcell'
     case '099':
        company="bakcell"
     case "070":
         company="nar"
     case "077":
        company='nar'
     case _:
        company='not found'
    if company=="not found":
      print('Wrong prefix')
    else:
     print("Phone number accepted")