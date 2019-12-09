def countingValleys(n, s):
  level = 0
  valleys = 0
  for step in s:
    if step == 'U':
      if level == -1:
        valleys +=1
      level +=1
    else:
      level -= 1
  return valleys

print(countingValleys(8,  'UDDDUDUU'))
