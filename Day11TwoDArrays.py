
if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

count = 0
max_count = -63

for i in range(0, len(arr)-2):
    for j in range(0, len(arr[i])-2):
        count = ((arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                            + arr[i + 1][j + 1]
            + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]))
        if count > max_count:
            max_count = count
print(max_count)



'''
mat1_1 = (arr[0][0]+arr[0][1]+arr[0][2]
        +arr[1][1]
        +arr[2][0]+arr[2][1]+arr[2][2])

mat1_2 = (arr[0][1]+arr[0][2]+arr[0][3]
        +arr[1][2]
        +arr[2][1]+arr[2][2]+arr[2][3])

mat1_3 = (arr[0][2]+arr[0][3]+arr[0][4]
        +arr[1][3]
        +arr[2][1]+arr[2][2]+arr[2][3])

mat1_4= (arr[i][j]+arr[i][j+1]+arr[i][j+2]
        +arr[i+1][j+2]
        +arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])


mat2_1=
'''

'''
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
'''