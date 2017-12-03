def between_markers(text, begin,end):
	if begin in text and end in text:
		return text[text.find(begin)+len(begin):text.find(end)]
	elif begin in text and not end in text:
		return text[text.find(begin)+len(begin):]
	elif not begin in text and end in text:
		return text[:text.find(end)]
	else:
		return text


if __name__ == '__main__':
	print(between_markers('What is >apple<', '>', '<'))
	print(between_markers('What is >apple lala', '>', '<'))
	print(between_markers('What is apple<', '>', '<'))
	print(between_markers('What is apple', '>', '<'))