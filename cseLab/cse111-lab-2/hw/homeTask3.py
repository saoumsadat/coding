def assign_students_to_sections(section, *names):
	d = dict()
	for x in section:
		d[x] = []
	for name in names:
		sum = 0
		for x in name:
			sum += ord(x)
		ind = sum % 5
		d[section[ind]].append(name)
	return d

final_dict = assign_students_to_sections('ABCDE', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace')
print(final_dict)