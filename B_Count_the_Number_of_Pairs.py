from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter

def solve():
    n, k = II()
    s = S()

    counter = Counter(s)
    left = 0
    count = 0
    
    for char in "abcdefghijklmnopqrstuvwxyz":
        lower = counter[char]
        upper = counter[chr(ord(char) - 32)]
        mini = min(lower, upper)
        count += min(lower, upper)
        lower -= mini
        upper -= mini
        if lower != 0:
            left += lower // 2
        
        if upper != 0:
            left += upper // 2

    
    count += min(left, k)

    print(count)

 
 
  
 
T = I()
for _ in range(T):
    solve()