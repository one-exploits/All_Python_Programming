from tkinter import *
import os;
class Color:
	c1="#40E0D0";
	
####GUIwindow####
window=Tk();
#set width=x && set height=y
window.geometry()
window.maxsize()
window.minsize()
tlab=Label(text='''Inspiration is one thing and you can't control it,
\n but hard work is what keeps the ship moving.
\n  Good luck means, work hard. Keep up the good work.Read more at 
\n Thanks\n{}'''.format(os.getcwd()),bg="white",fg=Color.c1,padx=1000,pady=200,font="commicsansms 7 bold");
tlab.pack()
window.configure(bg=Color.c1)
window.mainloop();