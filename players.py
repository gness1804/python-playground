titles = {
  'Lebron James': 3,
  'Tom Brady': 6,
  'Anthony Davis': 0,
}

def findWinless(obj):
  '''Shows each player who has not yet won a title.'''
  for player in titles:
    if titles[player] == 0:
      print(player + ' has not won a title yet.')

findWinless(titles)
