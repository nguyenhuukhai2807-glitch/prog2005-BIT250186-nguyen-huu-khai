def hinh1(n=4):
    for i in range(n):
        for j in range(n):
            print(1, end=' ')
        print()
def hinh2(n=4):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(j, end=' ')
        print()
def hinh3(n=4):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
def hinh4(n=4):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
def hinh6(n=4):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j == 1 or i == 1 or j == n or i == n:
                print(j, end=' ')
            else:
                print(' ', end=' ')
            print()
def hinh7(n=4):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j == i:
                print(i, end=' ')
            else:
                print(' ', end=' ')
        print()
def hinh8(n=4):
    for i in range(1, n+1):
        for s in range(n-i):
            print(' ', end=' ')
        for j in range(1, i+1):
            print(j, end=' ')
        for j in range(i-1, 0, -1):
            print(j, end=' ')
        print()
def hinh9(n=4):
    for i in range(1, n+1):
        for s in range(n-i):
            print(' ', end=' ')
        for j in range(1, i+1):
            print(j, end=' ')
        for j in range(i-1, 0, -1):
            print(j, end=' ')
        print()