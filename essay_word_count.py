while True:
    s = input()


    s = s.split(" ")

    count = 0

    for word in s:
        count = word.count()
    
    print(count)

