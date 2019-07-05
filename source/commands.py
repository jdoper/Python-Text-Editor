import labels
import helpers
from tkinter import *

class SaveCommand:
    def __init__(self, root, text):
        self.root = root
        self.text = text
        self.action = helpers.DocumentSaveAs(self.text)

    def configure(self):
        # adicionando item na interface
        button = Button(
            self.root, text=labels.SAVEAS_LABEL, command=self.action.save
        )
        button.grid()

class ChangeFontCommand:
    def __init__(self, root, text):
        self.root = root
        self.text = text
        self.action = helpers.EditorConigurator(self.text)
        self.courier = IntVar()
        self.helvetica = IntVar()
    
    def add_options(self, font):
        # inserindo opções no seletor de fonte
        font.menu = Menu(font, tearoff=0)
        font["menu"] = font.menu
        font.menu.add_checkbutton(
            label="Courier", variable=self.courier, command=self.action.fontCourier
        )
        font.menu.add_checkbutton(
            label="Helvetica", variable=self.helvetica, command=self.action.fontHelvetica
        )

    def configure(self):
        # adicionando item na interface
        font = Menubutton(self.root, text=labels.FONT_LABEL)
        font.grid()
        self.add_options(font)