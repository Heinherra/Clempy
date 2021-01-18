import sys
#print(sys.path)
#sys.path.insert(1,sys.path[0])

from modules.webhook import moduleB as B


try:
        instance
        t
except NameError:
        t = 0
        instance = None

def set_instance(module):
	global instance
	instance = module

def other_test():
	instance.test()

def test():
    global t
    t += 1
    print("Test from A")

