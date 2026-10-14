from sys import stdin

def I(): return int(stdin.readline().strip())

def IL(): return list(map(int, stdin.readline().strip().split()))

def main():
    test_cases = I()
    answer = []

    def doSquare(i, arr, n):
        if i == n:
            return 0
        num = arr[i]
        if num > 0:
            return num * num + doSquare(i + 1, arr, n)
        else:
            return doSquare(i + 1, arr, n)
        
    def takeInputList(sofar):
        if sofar == test_cases:
            return
        n = I()
        a = IL()
        answer.append(doSquare(0, a, n))
        takeInputList(sofar + 1)
        
    
    takeInputList(0)

    def printAnswer(answer, i):
        if i == test_cases:
            return
        print(answer[i])
        printAnswer(answer, i + 1)
    
    printAnswer(answer, 0)
    

    

if __name__ == "__main__":
    main()