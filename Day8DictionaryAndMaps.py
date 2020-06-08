n = int(input())
my_dict = {}
if n >= 1:
    for i in range(0, n):
        # name_number = input()
        # key, value = name_number.split(" ")
        key, value = input().split(" ")
        if len(value) == 8:
            my_dict[key] = value

    while True:
        try:
            search_name = input()
        except EOFError as error:
            break
        if search_name in my_dict:
            print(search_name+'='+my_dict[search_name])
        else:
            print('Not found')



"""

n = int(input())
my_dict = {}
if n >= 1:
    for i in range(0, n):
        name_number = input()
        key, value = name_number.split(" ")
        if len(value) == 8:
            my_dict[key] = value

    search_name = input()

    while search_name != '':
        if search_name in my_dict:
            print(search_name+'='+my_dict[search_name])
        else:
            print('Not found')
        search_name = input()


sample input:
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
"""

"""
sample output:
sam=99912222
Not found
harry=12299933
"""