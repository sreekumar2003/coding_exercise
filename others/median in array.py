a = [10,24,76,97,34,56]
a.sort()
l = len(a)
l2 = len(a)//2
if l % 2!=0:
    med = l//2
    print(a[med])
else:
    med = (a[l2]+a[l2-1])//2
    print(med)
