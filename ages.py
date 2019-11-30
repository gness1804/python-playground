count = 0
ages = [69, 64, 37, 31, 26]

for age in ages:
  count += age

print(str(count) + ' is the total age.')

ages2 = [78, 34, 17, 32, 49]

adults = []

for item in ages2:
  if item >= 18:
    adults.append(item)

print(adults)

for i in range(4):
  print(i)

for age in ages2:
  if age < 40:
    print(str(age) + ' Still young!')
    break
else:
  print(str(age) + ' Young at heart...') # never hits because the loop breaks earlier

