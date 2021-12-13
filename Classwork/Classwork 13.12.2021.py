'''
# Homework 13.12.2021
# Task 1 - Lucky tickets

arr = [3,1,0,0,0,4]

if sum(arr[0:3]) == sum(arr[3:6]):
    print(True)

else:
    print(False)

# Another way (Odd & even)

arr_odd = 0
arr_even = 0

for elem in arr:
    if elem % 2 == 0:
        arr_odd += elem

    else:
        arr_even += elem

if arr_odd == arr_even:
    print(True)

else:
    print(False)


# Task 2 - One extracting

arr_ones = [[1,2,3,4],[3,1,1]]
ones_ex = []

for arr in arr_ones:
    for number in arr:
        if number == 1:
            ones_ex.append(number)

print(f"Sum: {sum(ones_ex)}")

# Task 3 - Unique values
mass = [1,2,2,3,4,4,4,5,5,6]
mass_uniq = list(set(mass))
print(mass_uniq)


# Classwork

# Task - Sheep counting
from random import randint

sheeps = []
sheeps_count = 0
for sheep in range(randint(2,20)):
    sheeps.append(bool(randint(0,1)))

for sheep in sheeps:
    if sheep == True:
        sheeps_count += 1

# Task - Bugs
a = "code"
b = "wa.rs"
name = a + b
print(name)


# Dictionaries

dictionary = {'id':1, 'name':'Oleg', 'age':20}
print(dictionary['age'])

print(dictionary.keys())

print(dictionary.values())

dictionary_new = dict.fromkeys(['name', 'surename', 'age'], None)

print(dictionary_new)
'''

