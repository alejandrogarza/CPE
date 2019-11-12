# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    left_sum = 0
    right_sum = sum(A)
    difference_values = []
    for i in range(0, len(A)-1):
        left_sum += A[i]
        right_sum -= A[i]
        difference = left_sum - right_sum
        difference_values.append(abs(difference))
    return min(difference_values)
    pass
