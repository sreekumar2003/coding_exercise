num  = int(input("Enter the number: "))
count = 0
for i in range(1,num+1):
    if i % 3==0:
        count += 1
print(count)
