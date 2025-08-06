num=int(input("Enter the number: "))
reverse=0
while num>0:
    temp = num%10
    num = num//10
    reverse = reverse*10+temp
print(reverse)
    
