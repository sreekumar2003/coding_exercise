n = int(input("Enter the number of elements: "))
a = []
for i in range(n):
     c = int(input("Enter the number: "))
     a.append(c)
k = int(input("Enter the rotation: "))
for i in range(k):
    temp = a.pop()
    a.insert(0, temp)
    print(a)
print(a)
'''
Enter the number of elements: 5
Enter the number: 1
Enter the number: 2
Enter the number: 3
Enter the number: 4
Enter the number: 5
Enter the rotation: 4
[5, 1, 2, 3, 4]
[4, 5, 1, 2, 3]
[3, 4, 5, 1, 2]
[2, 3, 4, 5, 1]
[2, 3, 4, 5, 1]
'''
