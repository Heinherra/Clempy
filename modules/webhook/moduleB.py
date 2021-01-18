t = 0

try:
        instance
         
except NameError:
        instance = None
def set_instance(module):
	global instance
	instance = module

def other_test():
	instance.test()

def test():
    global t
    t += 1
    print("Test from B")
