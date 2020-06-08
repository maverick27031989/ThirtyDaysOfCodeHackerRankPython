class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        minValue = 101
        maxValue = 0
        for ele in self.__elements:
            if ele < minValue:
                minValue = ele
            if ele > maxValue:
                maxValue = ele
        self.maximumDifference = maxValue-minValue


# End of Difference class
N = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
