import statistics as st
arr1 = [3,5,2,2,45,6]
arr2 = [5,3,2,4,5,2,6]

arr1.extend(arr2)
arr1.sort()
print(st.median(arr1))

print(arr1)

m = len(arr1)
if m%2 == 0:
    print((arr1[m//2-1]+ arr1[m//2])/2)
else:
    print(arr1[m//2])
