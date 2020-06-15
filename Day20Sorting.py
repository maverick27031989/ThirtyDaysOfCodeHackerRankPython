import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

totalNumOfSwap = 0
for i in range(0, n):
    numSwap = 0
    temp = 0
    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            numSwap = numSwap + 1
    totalNumOfSwap += numSwap

    if numSwap == 0:
        break

print('Array is sorted in', totalNumOfSwap, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])

