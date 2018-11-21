import os
import py3nvml
import time
import sys

def safe_int(s, default_value=0):
	try:
		return int(s)
	except:
		return default_value

def find_idle_cpus(num_cpus=10, wait_time_seconds=0.6):
	
	with open('/proc/stat', 'r') as fh: # see https://linux.die.net/man/5/proc how to interpret this
		lines = fh.readlines()
		cpulines = [ line.strip().split(" ") for line in lines if line.startswith('cpu') ][1:]
		cpu_ids = [ cpuinfo[0][3:] for cpuinfo in cpulines ]
		idle_time_start = [ safe_int(cpuinfo[4], 0) for cpuinfo in cpulines ]
	time.sleep(wait_time_seconds)
	with open('/proc/stat', 'r') as fh: # see https://linux.die.net/man/5/proc how to interpret this
		lines = fh.readlines()
		cpulines = [ line.strip().split(" ") for line in lines if line.startswith('cpu') ][1:]
		idle_time_stop = [ safe_int(cpuinfo[4], idle_time_start[i]) for i, cpuinfo in enumerate(cpulines) ]
	cpu_idle_info = [ ( idle_time_stop[i]-idle_time_start[i], cpu_id) for i, cpu_id in enumerate(cpu_ids) ]
	cpu_idle_info.sort(reverse=True)
	return cpu_idle_info	
			

if __name__=='__main__':
	if len(sys.argv)<3:
		print("Missing arguments: [cpu-count] [gpu-count]")
		sys.exit(1)
	cpu_count = int(sys.argv[1])
	gpu_count = int(sys.argv[2])
	argv_rest = sys.argv[2:]
	cpu_idle_info = find_idle_cpus(0.5)
	my_pid = os.getpid()
	cpu_list = ",".join([ cpu_idle_count[1] for cpu_idle_count in cpu_idle_info[:cpu_count] ])
	argv = []+sys.argv
	command = [ "taskset", "-a", "-c", cpu_list ] + argv[3:]
	#print(command)
	py3nvml.grab_gpus(num_gpus=gpu_count, gpu_fraction=0.95)
	environ = dict(os.environ)
	
	environ['LD_PRELOAD'] = os.path.abspath(os.path.dirname(__file__)) + "/limit_visible_cpus.so"
	environ['OMP_NUM_THREADS'] = str(cpu_count)
	# This call never returns.
	os.execvpe(command[0], command, environ)
