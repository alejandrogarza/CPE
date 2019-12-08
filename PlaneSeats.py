# You are processing plane seat reservations. The
# plane has N rows of seats, numbered from 1 to
# N. There are ten in each row (labelled from 
# A to K, with letter I omitted). as shown in the
# figure below: 

# https://i.imgur.com/4MColZ7.png

# Some of the seats are already reserved. The list
# of reserved seats is given as a string S (of length
# M) containing seat numbers separated by single
# spaces: for example: "1A 3C 2B 40G 5A".
# The reserved seats can be listed in S in any order.

# Your task is to allocate seats for as many four-
# person families as possible. A four-person family
# occupies four seats in one row, that are next to
# each other - seasts across an aisle(such as 2c 
# and 2D) are not considered to be next to each 
# other. It is permissible for the family to be
# separated by an aisle, but in this case exactly
# two people have to sit on each side of the aisle.
# Obviously, no seat can be allocated to more than
# one family

# Write a function
# def solution(N, S):

# that given the number of rows N ansd a list of 
# reserved seats as String S, return the maximum 
# number of four-person families that can be
# seated in the remaining unreserved seats. 

# For instance, given N = 2 and S = "1A 2F 1C",
# your function should return 2. The following
# figure shows one possible way of seating four
# families in the remaining seats:

# https://i.imgur.com/YtpH8t4.png

# Given N = 1 and S = "" (empty string, your
# function should return 2, because we can seat at
# most two families in a single row of seats, as
# shown in the figure below: 

# https://i.imgur.com/KtgtCnx.png

# Assume that: 
# - N is an integer within the range [1..50];
# - M is an integer within the range [0..1, 909];
# - string S consists of valid seat names separated with single spaces;
# - every seat number appears in string S at most once

def solution(N, S):
  if not S:
      return 4 * N

  family_count = 0
  seats = S.split()
  for row in range(1, N+1):
    is_middle_free = 1
    if (str(row) + str('B') not in seats) and (str(row) + str('C') not in seats) and (str(row) + str('D') not in seats) and (str(row) + str('E') not in seats):
      family_count += 1
      is_middle_free = 0

    if (str(row) + str('F') not in seats) and (str(row) + str('G') not in seats) and (str(row) + str('H') not in seats) and (str(row) + str('J') not in seats):
      family_count += 1
      is_middle_free = 0

    if is_middle_free and (str(row) + str('D') not in seats) and (str(row) + str('E') not in seats) and (str(row) + str('F') not in seats) and (str(row) + str('G') not in seats):
      family_count += 1
    
  return family_count


print(solution(2, "1A 2F 1C"))
