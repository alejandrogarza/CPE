# Given an array of numbers, return the first unique instance. 

def solution(lst):
    counts = {}

    for item in lst:
      if item in counts:
          counts[item] += 1
      else:
          counts[item] = 1

    for item in lst:
      if counts[item] == 1:
          return item
          
print(solution([1,2,1,3,2,5]))
print(solution([1,2,6,1,3,3,2,5]))
print(solution([1,2,1,3,3,2,5,5]))
print(solution([7]))
