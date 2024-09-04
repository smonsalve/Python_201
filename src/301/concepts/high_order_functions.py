# numbers = [3,5,7,12,18,20,21]

# squared = map(lambda num: num**2, numbers)

# print(list(squared))


odd_nums = filter(lambda num: num % 2 != 0, range(1, 21))
print(list(odd_nums))