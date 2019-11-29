import random

userNum = int(input('Please enter a number between 1 and 100.'))
print(userNum)
randomNum = random.random() * 100
print(round(randomNum, 0))

if userNum < randomNum:
  print('Too low.')
elif userNum > randomNum:
    print('Too high.')
else:
  print('You win!')
