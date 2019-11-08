# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    binary = str(bin(N)[2:])
    max_zeros_array = []
    amount_zeros = 0
    initial_one = False
    closed_one = False
    for char in binary:
      if(not initial_one):
        if char == "1":
          initial_one = True
          continue
      else:
        if char == "0":
          amount_zeros += 1
        else:
          max_zeros_array.append(amount_zeros)
          amount_zeros = 0
          
    if len(max_zeros_array):
        return max(max_zeros_array)
    else:
        return 0
