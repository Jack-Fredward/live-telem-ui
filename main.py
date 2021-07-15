import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

LARGEFONT =("Verdana", 35) 
SMALLFONT =("calibre",10)

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
		mainLabel.grid(row=0, column = 4, padx = 10, pady=10)

def main():
	app = LiveTelemUI()
	app.mainloop()

main()