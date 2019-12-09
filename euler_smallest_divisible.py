# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def solution(n):
  all_factors = []
  for i in range(1, n+1):
    all_factors.append(i)

  for num in range(n, 99999999999999, n):
    if all(num % i == 0 for i in all_factors):
      return num

print(solution(10)) # 2520
print(solution(20)) # 232792560
