import re
import time

print("hallo mahmoud")
time1=time.time
print("hallo mahmoud ")



from tkinter import *

fenster = Tk()

variable = StringVar(fenster)
variable.set("one") # default value

w = OptionMenu(fenster, variable, "one", "two", "three")
w.pack()

fenster.mainloop()