t = int(input())
for i in range (t):
    si1 = int(input())
    s1 = set(map(int,input().split()))
    si2 = int(input())
    s2 = set(map(int,input().split()))        
    if len(s1.difference(s2))>0:
        print("False")
    else:
        print("True")
'''
input
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

output

True
False
False
''''


