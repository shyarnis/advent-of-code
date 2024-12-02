with open("input.txt", "r") as f:
    array = []
    for line in f:
        row = []
        for i in line.split():
            row.append(int(i))

        array.append(row)


# Safe Count
count = 0
for i in range(len(array)):
    isSafe = True
    # print(array[i])
    for j in range(1, len(array[i])):
        diff = abs(array[i][j] - array[i][j - 1])

        if diff == 0 or diff > 3:
            isSafe = False

        # check shift in direction of numbers.
        if ((array[i][1] - array[i][0]) * (array[i][j] - array[i][j - 1])) < 0:
            isSafe = False

    if isSafe:
        count += 1


print(count)
