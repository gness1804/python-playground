def describeCat(type, *args, **keywords):
  print('This cat is of the type ' + type)
  for arg in args:
    print('It is quite ' + arg)

  for word in keywords:
    print(word + ': ' + str(keywords[word]))


describeCat('Tabby', 'Moody', 'Playful',  color='Orange', weightInLb=13, sex='male', fixed=True)
