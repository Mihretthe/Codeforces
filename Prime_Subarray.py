from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    index = 5

    while index * index < num:
        if num % index == 0:
            return False
        index += 6
    
    return True



def solve():
    s = (S()[7:-1])
    a = list(map(int, s.split(",")))

 
    left = 0
    count = 0
    total = 0

    for right in range(len(a)):
        total += a[right]
        
        while left < len(a) and not isPrime(total):
            
            total -= a[left]
            left += 1
        
        count += (right - left + 1)
    n = len(a)

    print(n * (n + 1) // 2) # 1 2 3 12 123 23
    print(count)


 
 
T = 1
for _ in range(T):
    solve()