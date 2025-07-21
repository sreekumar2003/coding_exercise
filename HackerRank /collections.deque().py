from collections import deque

n = int(input())
d = deque()


for _ in range(n):
    fun = input().split()
    if fun[0]=='append':
        d.append(int(fun[1]))
    elif fun[0]=='appendleft':
        d.appendleft(int(fun[1]))
    elif fun[0]=='pop':
        d.pop()
        
    elif fun[0]=='popleft':
        d.popleft()       
        
for i in d:
    print(i,end=" ") 

'''
input

6
append 1
append 2
append 3
appendleft 4
pop
popleft

output

1 2

'''
