import re


with open("input.txt", "r") as f:
    text = f.read()


# detct mul(num1, num2) with regex.
# number should be 1-3 digit numbers.
pattern = r"mul\(\d{1,3}\,\d{1,3}\)|don't\(\)|do\(\)"
mulMatch = re.findall(pattern, text)


result = 0
isSkip = False

for i in mulMatch:
    if i == "don't()":
        isSkip = True
        continue

    if isSkip and i != "do()":
        continue

    if i == "do()":
        isSkip = False
        continue

    # for 1 digit numbers.
    # mul = int(i[4]) * int(i[-2])
    xy = i[4:-1].split(",")
    x = int(xy[0].strip())
    y = int(xy[1].strip())
    result += x * y

print(result)
