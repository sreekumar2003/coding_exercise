#Binary to Decimal converstion

num = int(input(("Enter the binary number: ")))
a = []
sum = 0
l = len(str(num))
m = l-1
num2 = [int(i) for i in str(num)]
print(num2)
for i in num2:
    a.append(i*2**m)
    m = m-1
print(a)
for i in a:
    sum = sum +i
print(sum)
