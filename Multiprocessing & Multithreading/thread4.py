from threading import *
def new():
    for i in range(6):
        print('Child Executing..',current_thread().getName())
        
t1 = Thread(target=new)
print(current_thread().getName())
t1.start()
t1.join()
print('Bye',current_thread().getName())
