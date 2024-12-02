with open("input.txt", "r") as f:
    array = []
    for line in f:
        row = [int(i) for i in line.split()]
        array.append(row)


# Safe Count
count = 0
for i in range(len(array)):
    isSafe = False
    isSafeWithoutRemoval = True

    # check if the row is already safe without removal
    for j in range(1, len(array[i])):
        diff = abs(array[i][j] - array[i][j - 1])

        if diff == 0 or diff > 3:
            isSafeWithoutRemoval = False

        # check shift in direction of numbers.
        if ((array[i][1] - array[i][0]) * (array[i][j] - array[i][j - 1])) < 0:
            isSafeWithoutRemoval = False

    # If the row is safe without removal, mark it as safe
    if isSafeWithoutRemoval:
        isSafe = True

    # else remove element from array, to make safe.
    else:
        for k in range(len(array[i])):
            newRow = array[i][:k] + array[i][k + 1 :]
            isSafeWithoutRemoval = True

            for j in range(1, len(newRow)):
                diff = abs(newRow[j] - newRow[j - 1])

                if diff == 0 or diff > 3:
                    isSafeWithoutRemoval = False

                # check shift in direction of numbers.
                if (newRow[1] - newRow[0]) * (newRow[j] - newRow[j - 1]) < 0:
                    isSafeWithoutRemoval = False

            # If removing one level makes it safe, mark it as safe
            if isSafeWithoutRemoval:
                isSafe = True
                break

    # final safe count.
    if isSafe:
        count += 1


print(count)
