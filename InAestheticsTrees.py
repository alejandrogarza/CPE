# Jimmy owns a garden in which he has planted N
# trees in a row. After a few years, the trees have
# grown up and now they have different heights.

# Jimmy pays much attention to the aesthetics of 
# his harden. He finds his trees aesthetically 
# pleasing if they alternately increase and 
# decrease in height (.., shorter, taller, shorter, 
# taller, ...).

# These exampels of aesthetically pleasing trees: 
# https://i.imgur.com/tpQfxCK.png

# Note that two adjacent trees cannot have equal
# heights. It may turn out that some trees have to
# be shortened in order to keep the look of the 
# garden aesthetically pleasing. Jimmy is a lazy
# type, so he wants to put as little energy as 
# possible into obtaining the desired look for his 
# garden. What is the minimum number of trees
# that should be shortened so that Jimmy would
# find his garden aesthetically pleasing?

# Write a function: 
# def solution(A)

# trhat given an Array A consisting of N integers 
# where A[K] denotes the height of the K-th tree,
# returns the minimum number of trees that
# should be shortened so that the garden looks aesthetically pleasing.

# Examples: 
# 1. Given A = [5, 4, 3, 2, 6] your function should 
# return 1. Jimmy can obtain the desired pattern
# by decreasing the height of the second tree to 2. 
# 2. Given A = [3, 7, 4, 5] your function should 
# return 0, since the garden already looks 
# aesthetically pleasing. 

# Write an *efficient* algorithm for the following assumptions: 
# N is an integer within the range [1...100,000];
# each element of Array A is an integer within the range [2...1,000].

def solution(A):
  ups = 0
  downs = 0
  changes = 0
  for i in range(len(A)-1):
    if (A[i+1] > A[i]):
      ups += 1
    elif A[i+1] < A[i]:
      downs += 1
    elif ups > downs:
      downs += 1
    elif downs > ups:
      ups += 1
    if ups - downs > 1 or downs - ups > 1:
      changes += 1
      ups = downs
  return changes


print(solution([5, 4, 3, 2, 6]))
print(solution([3, 7, 4, 5]))

