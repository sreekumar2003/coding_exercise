'''
input
3
1 0
2 $
3 1

output
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3 
'''

n = int(input())
for i in range(n):
    try:
        a,b=input().split()
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print(f'Error Code: {e}')
    except ValueError as e:
        print(f'Error Code: {e}')
