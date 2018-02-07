from flask import Flask, render_template
from time import localtime
from threading import Thread
import psutil

log = False
log_file = "logs/log_{}-{}-{}_{}:{}:{}.txt".format(localtime().tm_mday, localtime().tm_mon, localtime().tm_year, localtime().tm_hour, localtime().tm_min, localtime().tm_sec)
connection = 0

def write_log():
	cpu = psutil.cpu_percent(interval=1)
	memory = psutil.virtual_memory().percent
	global connection
	connection += 1
	data = "{},{},{}\n".format(connection, cpu, memory)
	f = open(log_file, "a+")
	f.write(data)
	f.close()

app = Flask(__name__)

@app.route('/')
def index():
	if log:
		t = Thread(target=write_log)
		t.start()
	return render_template("index.html")

if __name__ == '__main__':
	import sys
	try:
		if sys.argv[1] == "--log":
			log = True
			log_file = "logs/{}.txt".format(sys.argv[2])
			"""
			if sys.argv[2] == "true":
				log = True
			else:
				log = False
			"""
	except IndexError:
		log = False

	app.run(host='0.0.0.0', port=80)
