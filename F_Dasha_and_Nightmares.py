from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter

def solve():
    # one should be even, the other should be odd
    # the result of the concatination should have 25 unique characters
    # the count of each character should be odd

    n = I()
    array = []

    for _ in range(n):
        word = S()
        array.append(word)
    

    # represent the word with (26 bit checker for every letter availability, 26 bit checker for every letter evenness)
    # 
 
 
 
 
T = 1
for _ in range(T):
    solve()