num  = int(input("Enter the number: "))
temp = num
re = 0
while num>0:
    rem = num%10
    re = re*10 + rem
    num = num//10
print(re)
if re == temp:
    print("plaindrome")
else:
    print("not")
