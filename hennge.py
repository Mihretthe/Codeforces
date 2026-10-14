def calculate(array, index, n):
    if index == n:
        return 0

    if array[index] > 0:
        return calculate(array, index + 1, n)
    else:
        return powerOfFour(array[index]) + calculate(array, index + 1, n)

def powerOfFour(num):
    return num ** 4

def main():
    t = int(input())

    def testCases(i, t):
        if i == t:
            return 

        n = int(input())
        array = list(map(int, input().split()))
        
        print(calculate(array, 0, n))
        testCases(i + 1, t)

    testCases(0, t)
        






if __name__ == "__main__":
    main()