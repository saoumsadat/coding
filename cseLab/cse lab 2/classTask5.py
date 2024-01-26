# cgpa = float(input())
# credit = int(input())

# if (credit >= 30):
#     if (cgpa >= 3.80 and cgpa <= 3.89):
#         print("The student is eligible for a waiver of 25 percent")
#     elif (cgpa >= 3.90 and cgpa <= 3.94):
#         print("The student is eligible for a waiver of 50 percent")
#     elif (cgpa >= 3.95 and cgpa <= 3.99):
#         print("The student is eligible for a waiver of 75 percent")
#     elif (cgpa == 4.00):
#         print("The student is eligible for a waiver of 100 percent")
#     else:
#         print("The student is not eligible for a waiver")
# else:
#         print("The student is not eligible for a waiver")

cgpa = float(input())
credit = int(input())
percent = 0

if (credit >= 30):
    if (cgpa >= 3.80 and cgpa <= 3.89):
        percent = 25
    elif (cgpa >= 3.90 and cgpa <= 3.94):
        percent = 50
    elif (cgpa >= 3.95 and cgpa <= 3.99):
        percent = 75
    elif (cgpa == 4.00):
        percent = 100
    else:
        print("The student is not eligible for a waiver")
else:
    print("The student is not eligible for a waiver")

if percent != 0:
    print(f"The student is eligible for a waiver of {percent} percent")