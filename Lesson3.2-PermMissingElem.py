def solution(A):
    A = sorted(A)
    if len(A) < 1:
        return 1
    if len(A) == 1 and A[0] == 1:
      return A[0] + 1
    if A[0] > 1:
      return 1
    for i in range(0, len(A)):
        if i + 1 == len(A) or A[i+1] - A[i] > 1:
            return A[i] + 1
