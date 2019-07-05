import labels
import helpers
from tkinter import *

# configurando editor
root = Tk(labels.APP_NAME)
text = Text(root)
text.grid()

# ação para alterar fonte do editor
def fontCourier():
    text.config(font="Courier")

# ação para alterar fonte do editor
def fontHelvetica():
    text.config(font="Helvetica")

# adicioanndo seletor para alterar fonte
font = Menubutton(root, text=labels.FONT_LABEL)
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

# inserindo opções no seletor de fonte
courier = IntVar()
helvetica = IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier, command=fontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=fontHelvetica)

# adicionando botão "Save As" na interface
command_save = helpers.DocumentSaveAs(text)
button = Button(root, text=labels.SAVEAS_LABEL, command=command_save.save)
button.grid()

# executando editor
root.mainloop()