n = int(input())
md = 0
lst = []
while n >= 1:
    md = n % 2
    lst.append(md)
    n = n // 2
lst.reverse()
print(*lst, sep='')

count = 0
new_count = 0
for i in range(0, len(lst)):
    if lst[i] == 1:
        count += 1
        if count > new_count:
            new_count = count
    elif lst[i] == 0:
        if count > new_count:
            new_count = count
        count = 0
print(new_count)



# Recursive function
'''def bin(n):
    if n > 1:
        bin(n // 2)

    print(n % 2, end="")


if __name__ == "__main__":
    n = int(input())
    bin(n)
'''
