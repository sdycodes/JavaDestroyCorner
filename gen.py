import os
import random
num2ins = dict()
node_cand = []
TEST_DIR = "./tests/"
NODE_SIZE = 120
NODE_RANDGE_LOW = -200
NODE_RANDGE_HI = 200
cur_path_num = 10
def build_dicts():
	for i in range(NODE_SIZE):
		node_cand.append(random.randint(NODE_RANDGE_LOW, NODE_RANDGE_HI))
	num2ins[0] = "PATH_ADD"
	num2ins[1] = "PATH_REMOVE"
	num2ins[2] = "PATH_REMOVE_BY_ID"
	num2ins[3] = "PATH_GET_ID"
	num2ins[4] = "PATH_GET_BY_ID"
	num2ins[5] = "PATH_COUNT"
	num2ins[6] = "PATH_SIZE"
	num2ins[7] = "CONTAINS_PATH"
	num2ins[8] = "CONTAINS_PATH_ID"
	num2ins[9] = "DISTINCT_NODE_COUNT"
	num2ins[10] = "COMPARE_PATHS"
	num2ins[11] = "PATH_CONTAINS_NODE"
	num2ins[12] = "CONTAINS_NODE"
	num2ins[13] = "CONTAINS_EDGE"
	num2ins[14] = "IS_NODE_CONNECTED"
	num2ins[15] = "SHORTEST_PATH_LENGTH"
	num2ins[16] = "CONNECTED_BLOCK_COUNT"
	num2ins[17] = "LEAST_TICKET_PRICE"
	num2ins[18] = "LEAST_TRANSFER_COUNT"
	num2ins[19] = "LEAST_UNPLEASANT_VALUE"
	
def gen_one_ins():
	global cur_path_num
	ins_num = random.randint(0, len(num2ins) - 1)
	ins = num2ins[ins_num]
	if ins == "PATH_ADD":
		if cur_path_num > 80:
			return ins
		add_num = random.randint(3, 80)
		for i in range(add_num):
			node = node_cand[random.randint(0, NODE_SIZE - 1)]
			ins = ins + " " + str(node)
		cur_path_num += 1
	elif ins == "PATH_REMOVE":
		rm_num = random.randint(3, 80)
		for i in range(rm_num):
			node = node_cand[random.randint(0, NODE_SIZE - 1)]
			ins = ins + " " + str(node)
	
	elif ins == "PATH_GET_BY_ID" or ins == "PATH_REMOVE_BY_ID":
		ins += (" " + str(random.randint(1, cur_path_num)))
		
	elif ins == "PATH_COUNT":
		ins = "PATH_COUNT"
	
	elif ins == "PATH_SIZE":
		ins += (" " + str(random.randint(1, cur_path_num)))
		
	elif ins == "CONTAINS_PATH_ID":
		op = random.randint(0, 1)
		if op:
			ins += (" " + str(random.randint(1, cur_path_num)))
		else:
			ins += (" " + str(random.randint(cur_path_num, cur_path_num + 10)))
	
	elif ins == "COMPARE_PATHS":
		op1 = random.randint(1, cur_path_num)
		op2 = random.randint(1, cur_path_num)
		ins += (" " + str(op1) + " " + str(op2))
	
	elif ins == "PATH_CONTAINS_NODE":
		path = random.randint(1, cur_path_num)
		node = node_cand[random.randint(0, NODE_SIZE - 1)]
		ins += (" " + str(path) + " " + str(node))
		
	elif ins == "CONTAINS_NODE":
		node = node_cand[random.randint(0, NODE_SIZE - 1)]
		ins += (" " + str(node))

	elif ins == "CONTAINS_EDGE":
		src = node_cand[random.randint(0, NODE_SIZE - 1)]
		dst = node_cand[random.randint(0, NODE_SIZE - 1)]
		ins += (" " + str(src) + " " + str(dst))
		
	elif ins in ["IS_NODE_CONNECTED", "SHORTEST_PATH_LENGTH", "LEAST_TICKET_PRICE", "LEAST_TRANSFER_COUNT", "LEAST_UNPLEASANT_VALUE"]:
		src = node_cand[random.randint(0, NODE_SIZE - 1)]
		dst = node_cand[random.randint(0, NODE_SIZE - 1)]
		ins += (" " + str(src) + " " + str(dst))
	
	elif ins == "CONNECTED_BLOCK_COUNT":
		pass
	
	else:
		pass
	return ins
	
def gen_one_test(file_path, ins_num):
	global cur_path_num
	cur_path_num = 10
	with open(file_path, 'w') as f:
		for i in range(ins_num):
			ins = gen_one_ins()
			f.write(ins + "\n")
	
def gen_test(test_num, max_ins_per_test):
	for i in range(test_num):
		ins_num = random.randint(max_ins_per_test//2, max_ins_per_test) + 1;
		file_name = "t" + "%03d" %(i) + ".txt"
		gen_one_test(os.path.join(TEST_DIR, file_name), ins_num);
		
		
		
def gen(test_num, max_ins_per_test):
	build_dicts()
	gen_test(test_num, max_ins_per_test)
	

gen(10, 30000)
