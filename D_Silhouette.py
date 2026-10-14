from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter, defaultdict
from math import inf
from random import randint

def solve():
    n = I()
    a = IL()
    x = randint(1, 100)

    

    def write(key, val):
        
        for i in indexes[key ^ x]:
            answer[i] = val

        return val
    
    indexes = defaultdict(list)
    counter = defaultdict(int)

    for i in range(n):
        indexes[a[i] ^ x].append(i)
        counter[a[i] ^ x] += 1

    
    maxi = 0
    nums = sorted([i ^ x for i in counter])
    total = 0
    answer = [0] * n

    if 0 not in nums:
        print(-1)
        return 

    for i in range(1, len(nums)):
        before = nums[i - 1]
        countb = counter[before ^ x]
        current = nums[i]
        val = (current - total) // countb 

        if (current - total) % countb or val <= maxi:
            print(-1)
            return 

        write(before, val)
        total += (current - total)
        maxi = max(maxi, val)
        







    

    for i in range(n):
        if answer[i] == 0:
            answer[i] = maxi + 1
    print(*answer)



 
 
 
 
T = I()
for _ in range(T):
    solve()