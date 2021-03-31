import time
start = time.perf_counter()

def do_something():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done Sleeping')

do_something()
do_something()
do_something()
finish = time.perf_counter()
tt = finish-start
print('Finished in',round(tt,2))