with open("input.txt", "r") as file:
    nums = file.read().split(" ", 10)
result = 1
for num in nums:
    result *= int(num)
with open("output.txt", "w") as file:
    file.write(str(result))
