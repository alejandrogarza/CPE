
def solution(limit):
  numbers = []
  for i in range(limit):
    if i % 3 == 0 or i % 5 == 0:
      numbers.append(i)
  return sum(numbers)


print(solution(1000)) # 233168
