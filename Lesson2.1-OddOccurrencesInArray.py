def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]
    A = sorted(A)
    for i in range(0, len(A), 2):
        # if last one on the list or not the same
        if (i + 1) == len(A) or A[i] != A[i+1]:
            return A[i]
            
    # repeated_indexes = []
    # for i in range(len(A)):
    #     for j in range(len(A)):
    #         if i not in repeated_indexes and j not in repeated_indexes and i != j:
    #             if A[i] == A[j]:
    #                 repeated_indexes.append(i)
    #                 repeated_indexes.append(j)
                    
    # repeated_indexes = sorted(repeated_indexes)
    # for i in range(0, len(repeated_indexes)):
    #     if repeated_indexes[i] - i >= 1:
    #         return A[i]
