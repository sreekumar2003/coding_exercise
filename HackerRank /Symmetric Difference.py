n1 = int(input())
s1 = set(map(int, input().split()))


n2 = int(input())
s2 = set(map(int, input().split()))

s3 = s1.union(s2)
s4 = s1.intersection(s2)

s5 = s3.difference(s4)

s5 = list(s5)

s5.sort()
for i in s5:
    print(i)


'''
input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}


output

5
9
11
12

the output will in acsending order

'''
