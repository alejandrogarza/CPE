# in 36, there are 16 hourglasses
def hourglassSum(arr):
  max_sum = 0
  for i in range(0, len(arr)-2):
    for j in range(0, len(arr[i])-2):
      hourglass_sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
      if hourglass_sum > max_sum:
        max_sum = hourglass_sum
  return max_sum
