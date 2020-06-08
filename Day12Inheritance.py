class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        self.scores = scores

        Person.__init__(self, firstName, lastName, idNumber)

    def calculate(self):
        avg = sum(scores) / len(scores)
        grade = ''
        if avg < 40:
            grade = 'T'
        elif 40 <= avg < 55:
            grade = 'D'
        elif 55 <= avg < 70:
            grade = 'P'
        elif 70 <= avg < 80:
            grade = 'A'
        elif 80 <= avg < 90:
            grade = 'E'
        elif 90 <= avg <= 100:
            grade = 'O'
        return grade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
# numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)

s.printPerson()
print("Grade:", s.calculate())
