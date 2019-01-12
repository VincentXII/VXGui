from VXGUI import application, Task
from VXGUI.FileDialogs import request_old_file

def tick():
    print "Tick"

app = application()
task = Task(interval = 1, repeat = True, proc = tick)
result = request_old_file()
print "Result =", result
