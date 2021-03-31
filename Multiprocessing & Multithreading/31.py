import time
from multiprocessing import *
start = time.perf_counter()

def do_something():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done Sleeping')
    
p1 = Process(target=do_something)
p2 = Process(target=do_something)



p1.start()
p2.start()
	

finish = time.perf_counter()
tt = finish-start
print('finished in ',round(tt,2))