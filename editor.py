from tkinter import *
import tkinter.filedialog as fileDialog

root = Tk("Editor de Texto")
text = Text(root)
text.grid()

def saveas():
    global text_editor
    text_editor = text.get("1.0", "end-1c")
    savelocation = fileDialog.asksaveasfilename()

    file1 = open(savelocation, "w+")
    file1.write(text_editor)
    file1.close()

button = Button(root, text="Save", command=saveas)
button.grid()
root.mainloop()