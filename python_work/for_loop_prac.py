for value in range(1,21):
    print(value)

print()

a_million = list(range(1, 1000000))

print(min(a_million))
print(max(a_million))
print(sum(a_million))

odd_numbers = list(range(1,21,2))
for every_odd_numbers in odd_numbers:
    print(every_odd_numbers,"\n")

multiple_of_3 = [three for three in range(3,31,3)]
for three_multiple in multiple_of_3:
    print(three_multiple)

cubes =[]
for cubes_of_one_to_ten in range(1,11):
    cube = cubes_of_one_to_ten ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)

cubes_of_10 = [cube**3 for cube in range(1,11)]
print(cubes_of_10)