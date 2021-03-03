# 4-3
for value in range(1, 21):
    print(value)
# 4-4
numbers = list(range(1, 1_000_001))
'''for number in numbers:
    print(number)'''
# 4-5
print(min(numbers))
print(max(numbers))
print(sum(numbers))
# 4-6
odd_numbers = list(range(1, 21, 2))
for odd_number in odd_numbers:
    print(odd_number)
# 4-7
multiple_3 = list(range(3, 31, 3))
for multiple_of_3 in multiple_3:
    print(multiple_of_3)
# 4-8,4-9
cubes = list(value**3 for value in range(1, 11))
for cube in cubes:
    print(cube)



