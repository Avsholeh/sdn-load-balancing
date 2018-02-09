import sys

FILENAME = sys.argv[1]
f = open(FILENAME, "a+")
file = f.read()

cpu = list()
memory = list()

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

output = "Avg.Cpu: {} Avg.Mem {}".format(avg_cpu(), avg_mem())
print output
