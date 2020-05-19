def solution(A, B):
    # write your code in Python 3.6
    n = len(A)
    down = []
    res = 0
    for i in range(n):
        if B[i] == 0:
            while down and A[i] > down[-1]:
                down.pop()
            if not down:
                res += 1
        else:
            down.append(A[i])
    
    res += len(down)
    return res
    