def arrayLeaders(arr):
    leaders = []
    max_so_far = arr[-1]
    leaders.append(max_so_far)  # The rightmost element is always a leader
    
    # Traverse the array from right to left (second last to first)
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= max_so_far:
            leaders.append(arr[i])
            max_so_far = arr[i]  # Update max_so_far to the current leader
    
    return leaders[::-1]  # Reverse the leaders to get them in left-to-right order

# Example usage
arr = [16, 17, 4, 3, 5, 2]
print(arrayLeaders(arr))
