a = []
n = int(input("enter the rows: "))
m = int(input("Enter the columns: "))
for i in range (n):
    row=[]
    for i in range(m):
        element = int(input("Enter the nunbers: "))
        row.append(element)
    a.append(row)
    
for row in a:
    print(" ".join(map(str,row)))
    
mul=int(input("ENter the mul: "))
for i in range(n):
    for j in range(m):
        a[i][j]=mul*a[i][j]
        
for i in a:
    print(" ".join(map(str,i)))

