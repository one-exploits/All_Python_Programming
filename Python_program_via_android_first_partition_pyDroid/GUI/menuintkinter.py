from tkinter import*
import os
filenameexe=os.path.basename(__file__)
current=os.getcwd();
currentpath=current+str(filenameexe)
root=Tk();
root.title(currentpath);
menu=Menu(root,)
fileoption=Menu(menu,tearoff=0)
fileoption.add_command(label="New file")
fileoption.add_command(label="New Window")
fileoption.add_separator()
fileoption.add_command(label="Open File")
fileoption.add_command(label="Open folder")
fileoption.add_command(label="Open Recent")
fileoption.add_separator()
fileoption.add_command(label="Add Folder to Workspace")
fileoption.add_command(label="Save Workspace As...");
fileoption.add_separator();

fileoption.add_command(label="Save")
fileoption.add_command(label="Save As...")
fileoption.add_command(label="Save All")
fileoption.add_separator()
fileoption.add_command(label="Auto Save")
fileoption.add_command(label="Preference")
fileoption.add_separator()


fileoption.add_command(label="Revert File")
fileoption.add_command(label="Close Editor")
fileoption.add_command(label="Close Folder")
fileoption.add_command(label="Close Window")

fileoption.add_separator()


fileoption.add_command(label="Exit")


"""
##################################################################
########################edit option################################
###################################################################
"""
editoption=Menu(menu,tearoff=0)
editoption.add_command(label="Undo")
editoption.add_command(label="Redo")

editoption.add_separator()
editoption.add_command(label="Cut")
editoption.add_command(label="Copy")
editoption.add_command(label="Paste")
editoption.add_separator()


editoption.add_command(label="Find")
editoption.add_command(label="Replace")
editoption.add_separator()


editoption.add_command(label="Find in File")
editoption.add_command(label="Replace in File")
editoption.add_separator()

editoption.add_command(label="Toggle Line Comment")
editoption.add_command(label="Toggle Block Comment")
editoption.add_command(label="Emmet: Expand Abbreviation")
editoption.add_command(label="Emmet...")
"""
##################################################################
########################selection  option################################
######
"""
selection=Menu(menu,tearoff=0)
selection.add_command(label="Select All")
selection.add_command(label="Expand Selection")
selection.add_command(label="Shrink Selection")
selection.add_separator()



selection.add_command(label="Line Up")
selection.add_command(label="Line Down")
selection.add_command(label="Line Up")
selection.add_command(label="Line Down")
selection.add_separator()




selection.add_command(label="Add Cursor Above")
selection.add_command(label="Add Cursor Blew")
selection.add_command(label="Add Cursor Line Ends")
selection.add_command(label="Add Cursor To Line Ends")
selection.add_command(label="Add Next Occurrence")
selection.add_command(label="Add Previous Occurrence")
selection.add_command(label="Select All Occurrence")




menu.add_cascade(label="File",menu=fileoption)
menu.add_cascade(label="Edit",menu=editoption)
menu.add_cascade(label="Selection",menu=selection)


root.config(menu=menu)
e1=Entry(root)
e1.grid(row=0,column=1,pady=10)
root.mainloop()
