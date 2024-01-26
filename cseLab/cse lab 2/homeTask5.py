mark = int(input())
grade = ''
if mark <= 100 and mark >= 90:
    grade = "A"
elif mark <= 89 and mark >= 80:
    grade = "B"
elif mark <= 79 and mark >= 70:
    grade = "C"
elif mark <= 69 and mark >= 60:
    grade = "D"
elif mark <= 59 and mark >= 50:
    grade = "E"
elif mark < 50 and mark >= 0:
    grade = "F"
else:
    grade = "invalid"

print(grade)