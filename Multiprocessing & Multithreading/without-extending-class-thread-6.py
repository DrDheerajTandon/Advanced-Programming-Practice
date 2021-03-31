from threading import *
class Example:
    def fun(self):
        for i in range(5):
        	print('Child By: ',current_thread().getName())

E = Example()
t1 = Thread(target=E.fun)
t1.start()
t1.join()
print('Done by',current_thread().getName())
