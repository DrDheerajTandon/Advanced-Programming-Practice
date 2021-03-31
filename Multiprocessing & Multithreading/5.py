import time
from multiprocessing import *
start = time.perf_counter()

def do_something():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done Sleeping')


processes = []

if __name__ == '__main__':
	for _ in range(10):
		p = Process(target=do_something)
		p.start()
		processes.append(p)

	for process in processes:
		process.join()

finish = time.perf_counter()
tt = finish-start
print('finished in ',round(tt,2))
