titles = {
  'Lebron James': 3,
  'Dak Prescott': 0,
  'Tom Brady': 6,
  'Anthony Davis': 0,
}

def findWinless(obj):
  '''Shows each player who has not yet won a title.'''
  res = []
  for player in titles:
    if titles[player] == 0:
      res.append(player)
  return res

print(findWinless(titles))
