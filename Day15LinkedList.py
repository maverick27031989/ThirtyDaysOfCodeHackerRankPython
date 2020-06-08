class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        if head is None:
            head = Node(data)
        else:
            pntr = head
            while pntr.next is not None:
                pntr = pntr.next
            pntr.next = Node(data)
        return head


def traverse(head):
    pnttr = head
    while pnttr is not None:
        print(pnttr.data)
        pnttr = pnttr.next


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
#traverse(head)



'''
class Node:
    def __init__(self, info, link):
        self.info = info
        self.link = link


def main():
    node1 = Node(10, '')
    node2 = Node(15, '')
    node4 = Node(24, '')

    node1.link = node2
    node2.link = node4

    node3 = Node(55, '')
    # we have only pointer of node 2

    nod_4_pnt = node2.link
    node2.link = node3
    node3.link = nod_4_pnt

    traverse(node1)

    # count the number of elements in a linked list
    x = count(node1)
    print(x)

    # searching in a linked list
    search(node1, 77)


# traversing on linked list
def traverse(pointr):
    while pointr != '':
        print(pointr.info)
        pointr = pointr.link


def insert(head, new_node):
    pointr = head
    while pointr != '':
        pointr = pointr.link


# count the number of elements in a linked list
def count(ptr):
    num = 0
    while ptr != '':
        #        print(ptr.info)
        num = num + 1
        ptr = ptr.link
    return num


def search(pntr, item):
    while pntr != '':
        if pntr.info == item:
            print('Found')
            return
        pntr = pntr.link
    print('Not Found')


if __name__ == '__main__':
    main()
'''
