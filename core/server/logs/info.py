import sys

FILENAME = sys.argv[1]
f = open(FILENAME, "a+")
file = f.read()

#cpu = list()
#memory = list()
#index = 0
#image = 0

def split(data):
	container = list()
	for row in data:
		container.append(row.split(","))
	return container

data = split(file.split())

def avg_cpu():
	result = 0
	for item in data:
		result += float(item[1])
	result /= len(data)
	return result

def avg_mem():
	result = 0
	for item in data:
		result += float(item[2])
	result /= len(data)
	return result

def req_type():
	image = 0
	index = 0
	for item in data:
		if item[3] == "image":
			image += 1
		else:
			index += 1
	return [index, image]

output = "Avg.Cpu:{} Avg.Mem:{} Traffic:{} Index:{} Image:{}".format(avg_cpu(), avg_mem(), len(data), req_type()[0], req_type()[1])
print output
