from itertools import product

with open("input.txt", "r") as f:
    # words = [line.split(": ") for line in f]
    words = [line.strip().split(": ") for line in f]


result = 0
operators = ("+", "*")


for line in words:
    testValue = int(line[0])
    numbers = list(map(int, line[1].split()))

    # for each iteration, rotate the numbers.
    # to check to testValue from LHS.
    for ops in product(operators, repeat=len(numbers) - 1):
        # currentValue with rotate for each numbers from RHS.
        currentValue = numbers[0]

        for i, op in enumerate(ops):
            if op == "+":
                currentValue += numbers[i + 1]
            elif op == "*":
                currentValue *= numbers[i + 1]

        # if LHS equal to RHS.
        if currentValue == testValue:
            result += testValue
            break

print(result)
