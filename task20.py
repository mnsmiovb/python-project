studentID=input('Write your ID')
if len(studentID)==0:
    print('Student ID rejected.Input is empty')
elif len(studentID)!=8:
    print('Student ID rejected.It must be 8 digits')
elif not studentID.isdecimal() or not studentID.isascii():
    print('Student ID rejected.Only ASCII digits are allowed')
else:
    print("Student ID is accepted")
    