s = input("Enter the string: ")
a =[]
for i in s:
    c = s.count(i)
    if c >1:
        a.append(i)
a = set(a)
print("".join(a))
