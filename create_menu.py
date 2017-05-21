# TEAM SAAS 
from Tkinter import *


PROGRAM_NAME = "3D SCANNER"

root = Tk()
root.geometry('350x350')
root.title(PROGRAM_NAME)

menu_bar = Menu(root)  # menu begins

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit",command=root.quit)
# all file menu-items will be added here next
menu_bar.add_cascade(label='File', menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Setting")
menu_bar.add_cascade(label='Edit', menu=edit_menu)

about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label="Help")
menu_bar.add_cascade(label='About',  menu=about_menu)

root.config(menu=menu_bar)  # menu ends

root.mainloop()
