players = [
  {
    'name': 'Lebron James',
    'titles': 3,
    'current_team': 'Los Angeles Lakers'
  },
  {
    'name': 'Tony Parker',
    'titles': 4,
    'current_team': 'retired'
  },
  {
    'name': 'Anthony Davis',
    'titles': 0,
    'current_team': 'Los Angeles Lakers'
  },
  {
    'name': 'Hakeem Olajuwon',
    'titles': 2,
    'current_team': 'retired'
  },
]

def sortPlayers(_players):
  '''Sorts players by number of titles won.'''
  return sorted(_players, key=lambda player: player['titles'])

print(sortPlayers(players))
