n1 = input("enter the 1st number: ")
n2 = input("Enter the 2nd number: ")
c = 0
for i in range(int(n1),int(n2)):
    i = str(i)
    if i!=i[::-1]:
        print(i)
        c = c+1
print(c)

'''
enter the 1st number: 40
Enter the 2nd number: 45
40
41
42
43
4
'''
