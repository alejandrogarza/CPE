def lucky_floor(floor):
  until_floor = floor + 1
  i = 1
  while i < until_floor:
    if str(i).endswith('13') or  str(i).endswith('4'):
      until_floor += 1
    else:
      current_floor = i
    i += 1
  return current_floor

print(lucky_floor(12))
