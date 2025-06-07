def calcu (arr,target):
    ans = []
    n = len(arr)
    for i in range(n):
        sum = arr[i]
        for j in range(i+1,n):
            sum = sum + arr[j]
            if (sum==target):
                ans.append(i+1)
                ans.append(j+1)
                print(ans)
    if sum!=target:            
        print([-1])

    
    
arr = [15,2,4,8,9,5,10,23]
target = 23
calcu(arr,target)

#output
#[2,5]
