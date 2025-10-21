stone = [0, 1, 3, 5, 6, 8, 12, 17]
k = 1  # Initial jump distance (used for the first jump)

for i in range(1, len(stone)):
    flag = 1
    if i == 1:
        k = stone[1] - stone[0]  # First jump uses the actual distance
    else:
        k = stone[i - 1] - stone[i - 2]  # Use previous jump distance
    if stone[i - 1] + k + 1 == stone[i]:
        flag = 0
    elif stone[i - 1] + k == stone[i]:
        flag = 0
    elif stone[i - 1] + k - 1 == stone[i]:
        flag = 0
    if flag == 1:
        print('false')
        break
else:
    print('true')


# Question details is available  in the placement group 
