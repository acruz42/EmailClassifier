


def email_archiver(filename, parse):
	fil = open(filename, 'r')
	filText = fil.read()
	fil.close()
	#print (filText)

	index=0
	tagFinder = ''
	tag = ''
	content = ''
	archive = ''
	lineCounter = 0
	doubleLineCounter = 0
	body = False

	for c in filText[:len(filText)-1]:
		if c is '\n':
			tagFinder = filText[index+1]
			tag = ''
			lineCounter = lineCounter + 1

		if tagFinder is not '':
			tagFinder = tagFinder+c

		if c is ':':
			tag = tagFinder
			tagFinder = ''

		if tag == "F\nFrom:" or tag == "S\nSubject:":
			content = content + c

		if filText[abs(index-1)] is '\n' and filText[abs(index-2)] is '\n':
			doubleLineCounter = doubleLineCounter + 1
			if doubleLineCounter is 2:
				content = content + "\n"
				body = True

		if filText[index:index+3] == "--_":
			content = content[:len(content)-1]
			body = False

		if body is True:
			content = content + c

		index = index + 1
	content = content[:content.rfind(':')]+'\n'+content[content.rfind(':'):]
	content = content + "\n" + parse
	print (content)
	fil = open("archiveTest.txt",'w')
	fil.write(content)
	fil.close

			

email_archiver("1569539935.31017_2.mail", "Parse Type 1")
