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



