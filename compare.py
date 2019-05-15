import os
OUT_DIR = "./outputs"
def get_name():
	names = []
	raw_names = os.listdir("./jars")
	for each in raw_names:
		if each != "specs-homework-3-1.3-raw-jar-with-dependencies.jar" and each[0] != '.':
			names.append(each.split('.')[0])
	return names
	
def getlines(file_name):
	count = -1
	for count,line in enumerate(file_name):
		pass
	count += 1
	return count

	
def compare():
	test_num = len(os.listdir("./tests")) - 1
	names = get_name()
	for i in range(test_num):
		print("---round %03d---" %(i))
		comp_list = []
		files = []
		lines = -1
		validlines = 0
		for name in names:
			full = os.path.join(OUT_DIR, "%03d"%(i) + name + ".txt")
			print(full)
			comp_list.append(full)
		for f in comp_list:
			files.append(open(f, "r"))
		for f in files:
			if lines == -1:
				lines = getlines(f)
			elif lines != getlines(f):
				print("ERROR: t%03d.txt file line count not equal!" %(i))
				break
		files = []
		for f in comp_list:
			files.append(open(f, "r"))
		for lc in range(lines):
			res = []
			for f in files:
				res.append(f.readline())
			# print(res)
			if res[0][0] != 'F':
				validlines += 1
			for k in range(len(res)):
				for k2 in range(len(res)):
					if (res[k] != res[k2]):
						noreturn = res[k]
						if len(res[k]) > 1 and res[k][-1] == '\n':
							noreturn = res[k][0:len(res[k])-1]
						noreturn1 = res[k2]
						if len(res[k2]) > 1 and res[k2][-1] == '\n':
							noreturn1 = res[k2][0:len(res[k2])-1]
						print("ERROR: t%03d.txt, who %s %s, line: %d contents %s, %s" %(i, names[k], names[k2], lc + 1, noreturn, noreturn1))
		print("lines count: %d lines valid: %d" %(lines, validlines))
		for f in files:
			f.close()

compare()
