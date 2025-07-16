from itertools import product

n1 = list(map(int,input().split()))
n2 = list(map(int,input().split()))

c = (product(n1,n2)) 
for i in c:
    print(i,end=" ")

'''
input
1 2
3 4

output

