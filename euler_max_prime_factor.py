# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def solution(n):
  max_prime = 0
  factor = n
  i = 1
  while factor > 1:
    i += 1
    if factor % i == 0:
      if i > max_prime:
        max_prime = i
      factor = factor/i
      i = 1
  return max_prime

print(solution(13195)) # 29 
print(solution(600851475143)) # 6857
