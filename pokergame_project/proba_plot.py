#!/usr/bin/python
# -*- coding: utf8 -*-

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk             	

class PokerPlot:

    def get_image(self,image):

        self.image1 = image
   
   
    def makeplot2(self,**options):

        self.root = Tk.Toplevel()
        self.root.resizable(0,0)

        self.root.tk.call("wm", "iconphoto", self.root._w, self.image1)


        self.w = Tk.Frame(master=self.root,width=400,height=300)
        self.w.pack(side=Tk.RIGHT)

        self.f = Figure(figsize=(4,3), dpi=100)

        self.a2 = self.f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.f, master=self.w)

        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        self.canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

           
        self.a2.clear()    
        

        N = 3
        
        self.ind = np.arange(N)+0.5
        self.width = 0.35

        self.means=[]
                
        self.means.append(int(options.get("all1")))
        self.means.append(int(options.get("win")))
        self.means.append(int(options.get("lost")))
            
        self.means2 = np.array(self.means)
            
        self.rects1 = self.a2.bar(self.ind, self.means2, self.width, color=['b','g','r'])
        self.a2.set_title('Game statistics')
        self.a2.axis([0, 3, 0, max(self.means)+2])

        self.a2.set_xticks(np.arange(N)+0.7)
        self.a2.set_xticklabels(('All games','Win','Lost'))

        def autolabel(rects):
	    
	    for rect in rects:
	        height = rect.get_height()
		self.a2.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%i'%int(height),
			ha='center', va='bottom',size='8')

        autolabel(self.rects1)
   


        self.canvas.show()
        self.root.mainloop()
