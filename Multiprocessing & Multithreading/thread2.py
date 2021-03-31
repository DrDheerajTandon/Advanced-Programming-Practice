from threading import *
def new():
    for i in range(6):
        print('Child Executing..')
        
t1 = Thread(target=new)
t1.start()
t1.join()
print('Bye')
