from functools import reduce


nums = [1, 2, 3, 4, 5,1]

total = reduce(lambda acc, curr: acc + curr, nums)
print(total)