from threading import *
class A(Thread):
    def run(self):
        for i in range(5):
            print('Child: ',current_thread().getName())
obj = A()
obj.start()
obj.join()
print('Control returned to: ',current_thread().getName())

