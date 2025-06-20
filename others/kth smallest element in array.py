a = [12,34,234,354,2,34,46,1]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)
u = []

for i in a:
    if i not in u:
     u.append(i)
print(u)
k = int(input("Enter the kth elemwnt: "))
print(f'The {k}th element is {a[k-1]}')
