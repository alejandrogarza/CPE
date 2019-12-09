def sockMerchant(n, ar):
  count = {}
  pairs = 0
  for i in ar:
    if i in count:
      count[i] += 1
    else:
      count[i] = 1

  for i in count:
    pairs += int(count[i]/2)

  return pairs

print(sockMerchant(9, [10,20,20,10,10,30,50, 10,20]))
