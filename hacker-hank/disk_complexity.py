#!/usr/bin/python3

from collections import deque

def findMax(k, hardDiskSpace):
    n = len(hardDiskSpace)
    
    if n * k == 0 or k > n:
        return []

    deq = deque()
    res = []
    i = 0
    while i < n:
        if deq and deq[0] == i - k:
            deq.popleft()

        if deq and hardDiskSpace[deq[-1]] > hardDiskSpace[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            res.append(hardDiskSpace[deq[0]])
        
        i += 1
    
    return max(res)


if __name__ == '__main__':
    hdd = [62, 64, 77, 75, 71, 60, 79, 75]
    k = 4
    
    result = findMax(k, hdd)
    
    print(result)
