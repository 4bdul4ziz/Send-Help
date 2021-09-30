
import timeit

start = timeit.default_timer()


stop = timeit.default_timer()

print('Time: ', stop - start)

subs = []


def permute(a, l, r):
    if l == r:
        subs.append(list(a))
        # print("hi",list(a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]


def check(arr, y):
    count = 0
    for i in range(1, len(arr)+1):
        if arr[i-1] == i:
            count += 1
    if count == y:
        return True
    return False


def tes():
    x, y = input().split()
    x = int(x)
    y = int(y)
    arr = []
    for i in range(1, x+1):
        arr.append(i)
    permute(arr, 0, len(arr)-1)
    # print(subs)
    f = 0
    for i in subs:
        if check(i, y):
            print(*i)
            f = 1
            break
    if f == 0:
        print("-1")
    subs.clear()


t = int(input('\n'))
for i in range(t):
    tes()

stop = timeit.default_timer()

print('Time: ', stop - start)
