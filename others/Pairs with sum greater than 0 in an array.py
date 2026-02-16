arr = [-1,-1,-1,5]

arr.sort()

i,j,res = 0,len(arr)-1,0
while i<j:
    if arr[i]+arr[j]>0:
        res += (j-i)
        j -= 1
    else:
        i+= 1
print(res)


/*
ouput 3
*/
