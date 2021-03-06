import os
import subprocess
import multiprocessing
TEST_DIR = "./tests"
OUT_DIR = "./outputs"
JAR_DIR = "./jars"
	
def run(jar, input_file):
	cmdLine = "cat " + os.path.join(TEST_DIR, input_file) + " | (time java -jar " + os.path.join(JAR_DIR, jar) + ")"
	# print(cmdLine)
	path_name = input_file.split(".")[0]
	num = path_name.split('/')[-1]
	num = num[1:]
	res = subprocess.getoutput(cmdLine)
	all = res.split("\n\n")
	timeCount = all[-1]
	timeCount = timeCount.replace("\n", "| ")
	timeCount = "TIME of " + input_file + " " + jar + ": " + timeCount
	res = all[0]
	f = open("time.txt", "a")
	f.write(timeCount + "\n")
	f.close()
	print(timeCount)
	des = os.path.join(OUT_DIR, num + jar.split('.')[0]) + ".txt"
	f = open(des, "w")
	f.write(res)
	f.close()
	
def batchRun(nprocess = 3):
	jars = os.listdir(JAR_DIR)
	pool = multiprocessing.Pool(processes = nprocess)
	inputs = os.listdir(TEST_DIR)
	for inp in inputs:
		for each in jars:
			if each != "specs-homework-3-1.3-raw-jar-with-dependencies.jar" and each[0] != '.':
				pool.apply_async(run, (each, inp))
	pool.close()
	pool.join()
	
batchRun()
