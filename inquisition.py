def spanish_inquisition (expected=False, members=3, religion='Catholic') :
  _members = members
  if expected == False:
    print('Nobody expects the Spanish Inquisition!')
  if members > 3:
    _members = _members - 1
    print('Too many members! Your new membership is: ' + str(_members))
    spanish_inquisition(True, members=_members)
  else:
    print('The final membership number is: ' + str(_members))

spanish_inquisition(members=5)
