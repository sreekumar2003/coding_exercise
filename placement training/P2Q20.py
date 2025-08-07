num  = int(input("Enter the number: "))

while num>0:
    rem = num%10
    if rem%2 != 0:
        print("not even")
        break;
    num=num//10
print("its even")
        
    
