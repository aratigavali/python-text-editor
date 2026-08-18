#TEST EDITOR APP OR NOTEPAD APP 

#TKINTER MODULE OR LIBRARY - collection of module
#for creating gui apps 

import tkinter as tk

from tkinter import filedialog , messagebox

#main window code :

root = tk.Tk()
root.title("my text editor")
root.geometry("500x500")

#create text area
text=tk.Text(
    root ,
    wrap=tk.WORD,
    font=("helvetica" ,12 ),
    
)

text.pack(expand=True,fill=tk.BOTH)

#main logic 

#function - to create new file 

def newfile():
    text.delete(1.0,tk.END)

#fun 2 - to opennew file 

def openfile():
    #open file dialogue
    filepath = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("text files", "*.txt")]
    )

    if filepath:
        #open file 
        with open(filepath,"r") as file:
            #clear old text
            text.delete(1.0,tk.END)

            text.insert(tk.END,file.read())

#function 3 - save file 

def savefile():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("text file" , "*.txt")]
    )

    if filepath:
        with open(filepath,"w") as file :
            file.write(text.get(1.0,tk.END))


        messagebox.showinfo("info" , "file saved successfully")

#menu 

menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu,tearoff=0)

#new , openfile, save , esist

#add file  menu to menu bar 

menu.add_cascade(label="file" , menu=filemenu)

filemenu.add_command(label="New" , command=newfile)
filemenu.add_command(label="open" , command=openfile)
filemenu.add_command(label="save" , command=savefile)
filemenu.add_separator()
filemenu.add_command(label="exit" , command=root.quit)

# Edit menu

editmenu = tk.Menu(menu, tearoff=0)

menu.add_cascade(label="Edit", menu=editmenu)

editmenu.add_command(label="Cut", command=lambda: text.event_generate("<<Cut>>"))
editmenu.add_command(label="Copy", command=lambda: text.event_generate("<<Copy>>"))
editmenu.add_command(label="Paste", command=lambda: text.event_generate("<<Paste>>"))
editmenu.add_separator()
editmenu.add_command(label="Select All", command=lambda: text.event_generate("<<SelectAll>>"))

#start and keep window open 
root.mainloop()