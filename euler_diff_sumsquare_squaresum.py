# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def solution(n):
  all_numbers = []
  sum_of_square = 0
  for i in range(1, n+1):
    all_numbers.append(i)
    sum_of_square += i * i

  square_of_sum = sum(all_numbers) * sum(all_numbers)

  return square_of_sum - sum_of_square


print(solution(10)) # 2640
print(solution(100)) # 25164150
