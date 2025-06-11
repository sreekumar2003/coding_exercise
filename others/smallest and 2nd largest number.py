a=[5,7,2,1,7]
a.sort()
u = set()
for i in a:
    u.add(i)
a.clear()
for i in u:
    a.append(i)
print(a[0])
print(a[-2])
    
