import labels
import commands
from tkinter import *

# configurando editor
root = Tk(labels.APP_NAME)
text = Text(root)
text.grid()

# adicioanndo seletor para alterar fonte
command_font = commands.ChangeFontCommand(root, text)
command_font.configure()

# adicionando botão "Save As" na interface
command_save = commands.SaveCommand(root, text)
command_save.configure()

# executando editor
root.mainloop()