examScore=int(input("Write your exam score:"))
if examScore<0 or examScore>100:
    print('Invalid score')
else:
    result='pass' if examScore>=51 else 'fail'
    print(result)