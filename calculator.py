def arthematic_opration():
    print('start your calculation ;)')
    print('1.ADDITION')
    print('2.SUBRACTION')
    print('3.MULTIPLICATION')
    print('4.DIVISION')
    print('5.MODULO')
    print('6.FLOOR DIVISION')

    choice=int(input('Enter your choice: '))
    if choice==1:
        num1=float(input('enter first number: '))
        num2=float(input('Enter second number: '))
        print(f'sum of {num1} and {num2} is {num1+num2} ')

    elif choice==2:
        num1=float(input('enter first number: '))
        num2=float(input('Enter second number: '))
        print(f'difference of {num1} and {num2} is {num1-num2} ')
    elif choice==3:
        num1=float(input('enter first number: '))
        num2=float(input('Enter second number: '))
        print(f'product of {num1} and {num2} is {num1*num2} ')
    elif choice==4:
        num1=float(input('enter first number: '))
        num2=float(input('Enter second number: '))
        print(f'division of {num1} and {num2} is {num1/num2} ')
    elif choice==5:
        num1=float(input('enter first number: '))
        num2=float(input('Enter second number: '))
        print(f'modulo  of {num1} and {num2} is {num1%num2} ')
    elif choice==6:
        num1=float(input('enter first number: '))
        num2=float(input('Enter second number: '))
        print(f'floor division of {num1} and {num2} is {num1//num2} ')
    else: 
        print('please enter valid choice!!!!')
        arthematic_opration()
def repetation():
    user_choice=input('''If you want to continue please enter 'y' else enter'n' :''' )

    while user_choice=='y' or user_choice=='Y':
        arthematic_opration()
        user_choice=input('''If you want to continue please enter 'y' else enter'n' :''' )
    if user_choice=='n' or user_choice=='N':
        print('thank you for using the calculator')
    else:
        pass


arthematic_opration()
repetation()







