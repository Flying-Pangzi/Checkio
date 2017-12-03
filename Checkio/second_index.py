def func(string,char):
	str_list = list(string)
	count = 0
	for i in range(len(str_list)):
		if str_list[i] == char:
			if count != 0:
				return i
			count += 1

	if char == "" or count == len(str_list):
		return None






if __name__ == '__main__':
	print(func("find the river", "e"))
	print("lalala")
			



