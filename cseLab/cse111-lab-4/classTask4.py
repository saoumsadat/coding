class StudentDatabase:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = {}

    def calculateGPA(self, courseGradeList, session):
        courseList = []
        gradeList = []

        #distinguish course and grade
        for courseGrade in courseGradeList:
            courseList.append(courseGrade.split(': ')[0])
            gradeList.append(float(courseGrade.split(': ')[1]))

        #make courseTuple
        courseTuple = tuple(courseList)
        
        #calculate grade
        gradeSum = 0
        for grade in gradeList:
            gradeSum += grade * 3
        finalGrade = round(gradeSum / (len(gradeList) * 3), 2)
        
        #make value for final grades which is another dictionary
        gradeValue = {courseTuple: finalGrade}

        #finally add to the final dictionary
        self.grades[session] = gradeValue
    
    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")

        #accessing courseTuple of session keys
        for session in self.grades.keys():
            #printing session
            print(f"Courses taken in {session}:")
            
            for courses in self.grades[session].keys():
                for course in courses:
                    print(course)
                print(f"GPA: {self.grades[session][courses]}")
            



s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('---------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('---------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('---------------------------------')
s2.printDetails()
