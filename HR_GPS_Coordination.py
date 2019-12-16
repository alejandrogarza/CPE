def change_position(position, direction):
  if direction == 'R':
    position[0] += 1
  elif direction == 'L':
    position[0] -= 1
  elif direction == 'U':
    position[1] += 1
  elif direction == 'D':
    position[1] -= 1
  return position
  
def get_intersection(paths):
  path_length = min(len(paths['p1']['path']), 
  len(paths['p2']['path']))
  position_1 = paths['p1']['start']
  position_2 = paths['p2']['start']
  for i in range(path_length):
    position_1 = change_position(position_1, paths['p1']['path'][i])
    position_2 = change_position(position_2, paths['p2']['path'][i])
    if position_1 == position_2:
      return [position_1, i+1]
  return None



paths = {
  'p1': { 'start': [0,0], 'path': 'RUDURURU' },
  'p2': { 'start': [4,4], 'path': 'LDUDLDLD' }
}

print(get_intersection(paths))
