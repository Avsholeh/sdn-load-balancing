import psutil
import time

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent

while True:
    print cpu, memory
    time.sleep(1)
