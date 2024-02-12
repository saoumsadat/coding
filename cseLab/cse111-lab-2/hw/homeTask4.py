def username_generator(first_name, last_name, student_id, middle_name = ""):
	return first_name[0:3].upper() + middle_name + last_name[-3:].lower() + '_' + str(student_id)[-4:]

first_name, middle_name, last_name, student_id = input("First Name:"), input("Middle Name:"), input("Last Name:"), int(input ("Student ID:"))
# print(username_generator(first_name, last_name, student_id))
print(username_generator(first_name, last_name, student_id, middle_name))