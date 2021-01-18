import importlib as imp
import glob

modules = []

sep = "\\"

moduleNames = [f.replace("modules" + sep,"").replace(".py","") for f in glob.glob("modules"+sep+ "**"+ sep+ "*.py")]

tempNames = [name for name in moduleNames if not name.startswith("__") ]
moduleNames = tempNames

for name in moduleNames:
        module = imp.import_module('modules.' + name.replace(sep,"."))
        modules.append(module)

def main():
        for module in modules:
                call(module,"test")
        
        modules[0].set_instance(modules[1])
        modules[1].set_instance(modules[0])
        
        for module in modules:
                call(module,"other_test")
        
        for i in range(len(modules)):
                modules[i] = imp.reload(modules[i])

        for module in modules:
                call(module,"other_test")
        
        
        input()
        for i in range(len(modules)):
                modules[i] = imp.reload(modules[i])
        for module in modules:
                call(module,"test")
        
        modules[0].n = lambda x : x + 1
        print(modules[0].n(1))

def reimport(moduleNumber):
    modules[moduleNumber] = imp.import_module('modules.' + name.replace(sep,"."))


def catch():
        print("No such attribute")

def call(module ,function):
        print("Calling " + function)
        getattr(module, function, catch)()
        print()

main()

