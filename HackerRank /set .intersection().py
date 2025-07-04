n1 = int(input())
s1 = set(map(int,input().split()))
n2 = int(input())
s2 = set(map(int,input().split()))

s3 = s1.intersection(s2)

print(len(s3))

'''
input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

output

5

'''
