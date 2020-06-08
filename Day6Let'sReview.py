N = int(input())

for l in range(0, N):
    s = input()
    lst1 = []
    lst2 = []
    for i in range(0, len(s)):
        if i == 0 or i % 2 == 0:
            lst1.append(s[i])
        else:
            lst2.append(s[i])
    print(''.join(lst1) + ' ' + ''.join(lst2))
