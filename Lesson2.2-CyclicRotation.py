# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    if K == 0 or len(A) == 0:
        return A
        
    K = -K % len(A)
    return A[K:] + A[:K]
