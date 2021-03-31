from threading import *
class Example:
    def fun(self):
        l1 = [1,2,'d',4.5,'arvind']
        for i in l1:
            print(i
            
E = Example()
t1 = Thread(target=E.fun)
t1.start()
t1.join()
print('Done by',current_thread().getName())
