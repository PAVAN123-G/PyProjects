import datetime
print('****** WELCOME TO HEALTH MANAGEMENT SYSTEM ******')
def harry():
    F=input(f'enter the  code a for food and b for exercise\n')
    if F=='a':
        file = open('harryfood.txt', 'r')
        print(file.read())
        return datetime.datetime.now()
    elif F=='b':
        file = open('harryex.txt', 'r')
        print(file.read())
        return datetime.datetime.now()
    else:
        print('enter the correct input')
def rohan():
    F=input(f'enter the  code a for food and b for exercise\n')
    if F=='a':
        file = open('rohanfood.txt', 'r')
        print(file.read())
    elif F=='b':
        file = open('rohanex.txt', 'r')
        print(file.read())
    else:
        print('enter the correct input')
def hammad():
    F=input(f'enter the  code a for food and b for exercise\n')
    if F=='a':
        file = open('hammadfood.txt', 'r')
        print(file.read())
    elif F=='b':
        file = open('hammadex.txt', 'r')
        print(file.read())
    else:
        print('enter the correct input')
A=input('choose the name\n HARRY\t ROHAN\t HAMMAD\t')
if A=='HARRY':
    print(harry())
elif A=='ROHAN':
    print(rohan())
elif A=='HAMMAD':
    print(hammad())
else:
    print('you entered other person name which details is not present in database')




