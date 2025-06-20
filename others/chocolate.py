arr = [3,4,1,9,56,7,9,12]
arr.sort()
print(arr)
arr2 = []
arr3 = []
min = float('inf')
k = int(input("Enter the m number"))
for i in range(len(arr)-k+1):
    arr2 = arr[i:i+k]
    diff = arr2[-1]-arr2[0]
    if diff < min:
        min = diff
        arr3 = arr2
print(min)
print(arr3)

'''
Input: arr = [3, 4, 1, 9, 56, 7, 9, 12], m = 5
Output: 6
Explanation: The minimum difference between maximum chocolates and minimum chocolates is 9 - 3 = 6 by choosing following m packets :[3, 4, 9, 7, 9].
'''
