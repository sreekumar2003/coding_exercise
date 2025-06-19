num1 = int(input("enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
c = 0 

if num2%num1 == 0:
    print(f'The LCM is {num2}')
else:
    while c<1:
        num2 *= 2
        if num2%num1 == 0:
            print(f'The LCM is {num2}')
            c = 2
'''
enter the 1st number: 12
Enter the 2nd number: 15
The LCM is 60
'''
