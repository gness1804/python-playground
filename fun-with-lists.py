pets = ['Moley', 'Poley', 'Bob']

pets.extend(['Leon'])

print('pets with Leon added', pets)

pets.remove('Poley')

print('pets without Poley', pets)

nums = [3, 5, 33, 56, 3, 11, 903]

sortedNums = sorted(nums, key=lambda num: num % 2)
print(sortedNums) # [56, 3, 5, 33, 3, 11, 903]
