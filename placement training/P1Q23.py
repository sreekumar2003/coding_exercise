num=int(input("Enter the number: "))
if num in range(1,11):
    print("it is in the range 1-10")
elif num in range(11,21):
     print("it is in the range 11-20")
elif num in range(21,31):
     print("it is in the range 21-30")
else:
    print("It is above 30")
