/*
 * Given two integers, a and b, your task is to determine the sum of the cubes of
all numbers in the range from a to b.
sample test case
a = 4
b = 9
ouput: 1989
 */

a=int(input("enter the number"))
b = int (input("enter the number"))
sum = 0
for i in range(a,b+1):
    sum = sum + i**3
print(sum)
