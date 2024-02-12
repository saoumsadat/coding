def key_generator(*names):
	key_list = []
	for name in names:
		key = ''
		key += name[0].lower()
		for i in range((len(name) - 2), 0, -1):
			key += str(ord(name[i]))
		key += name[len(name) - 1].upper()
		key_list.append(key)
	return key_list

key_list = key_generator("Alex", "Bob", "Trudy")
print(key_list)