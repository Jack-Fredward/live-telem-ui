import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib
from matplotlib import figure
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasAgg, FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np
from random import seed
from random import *
import time


"""
TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO

write function for each subplots formatting for each time it is cleared need to put formatting back on
make a second figure with other subplots for more information
position gear better?
format
format
format

"""



# tk styling
LARGEFONT =("Verdana", 35) 
SMALLFONT =("calibre",10)

# global figure to get rid of later
f = Figure()
#ax1 = f.add_subplot(111)
f, ((ax1, ax2, ax3, ax4),(ax5, ax6, ax7, ax8)) = plt.subplots(2,4, sharex=True)

# f1 = Figure()
# f1, (ax5, ax6, ax7, ax8) = plt.subplots(4, sharex=True)
# ax1 = f.add_subplot(311)
# ax1.set_xlabel("Marks")
# ax1.set_ylabel("Students")
# ax1.set_title("Graph_Tk")
# ax1.grid()
# ax2 = f.add_subplot(312, sharex=ax1)
# ax3 = f.add_subplot(313, sharex=ax1)




# a = f.add_subplot(311)
# b = f.add_subplot(312)
# engineSpeed = f.add_subplot(511)
# inletManifoldPressure = f.add_subplot(512, sharex=engineSpeed)
# fuelPressure = f.add_subplot(513, sharex=inletManifoldPressure)
# engineOilPressure = f.add_subplot(514, sharex=fuelPressure)
# coolantTemp = f.add_subplot(515, sharex=engineOilPressure)

def updateData():
	file = open("sampleData.txt", "r+")
	x=len(file.readlines())+1
	# print(x)
	y = randint(0, 10)
	file.write(str(x)+','+str(y)+'\n')
	file.close()
	return x

def animate(i):
	xValue = updateData()
	pullData = open("sampleData.txt","r").read()
	dataList = pullData.split('\n')
	xList = []
	yList = []
	for eachLine in dataList:
		if len(eachLine)>1:
			x, y = eachLine.split(',')
			xList.append(int(x))
			yList.append(int(y))
	#want to test plotting three differetn sets of data at the same time.....ugh
	#could jsut generate three random numbers......
	for subplot in f.get_axes():
		# subplot.clear()
		subplot.cla()
		subplot.plot(xList[xValue-10:],yList[xValue-10:])
		# ((xValue%3+1)*10)
	# ax1.clear()
	# ax1.plot(xList[xValue-10:],yList[xValue-10:])

class LiveTelemUI(tk.Tk):
	# __init__ function for class tkinterApp 
	def __init__(self):
		# __init__ function for class Tk 
		tk.Tk.__init__(self)
		tk.Tk.wm_title(self, "Live Telemetry")

		# creating a container 
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 
		container.grid_rowconfigure(0, weight = 1) 
		container.grid_columnconfigure(0, weight = 1)

		# creating a menu bar
		menubar = tk.Menu(container)

		#file menu
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Exit", command = quit)
		menubar.add_cascade(label="File", menu=filemenu)

		tk.Tk.config(self, menu=menubar)


		# initializing frames to an empty array 
		self.frames = {}

		frame = StartPage(container, self)

		self.frames[StartPage] = frame

		frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		mainLabel = ttk.Label(self, text = "StartPage", font = LARGEFONT)
		mainLabel.grid(row=0, column = 0, padx = 10, pady=10)

		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)

		#displaying the graph in window
		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw()
		canvas.get_tk_widget().grid(row=1, column = 0, padx = 10, pady=10, columnspan=4, sticky=(N, S, E, W))
		canvas.get_tk_widget().columnconfigure(0, weight=1)
		canvas.get_tk_widget().rowconfigure(1, weight=1)

		#Gear Label
		gearLabel = ttk.Label(self, text = "Gear: ", font = LARGEFONT)
		gearLabel.grid(row=2, column = 0, padx = 10, pady=10)

		gearValue = ttk.Label(self, text = str(randint(1,5)), font = LARGEFONT)
		gearValue.grid(row=2, column = 1, padx = 10, pady=10)


#main
def main():
	app = LiveTelemUI()
	app.geometry("1280x760")
	#start in fullscreen windowed
	# app.state('zoomed')
	ani = animation.FuncAnimation(f, animate,interval=500)
	app.mainloop()
	

main()