import tkinter.filedialog as fileDialog

class DocumentSaveAs:
    def __init__(self, text):
        self.text = text
    
    def save(self):
        # recuperando texto inserido
        text_editor = self.text.get("1.0", "end-1c")
        savelocation = fileDialog.asksaveasfilename()

        # recuperando localização inserida e salvando arquivo
        file1 = open(savelocation, "w+")
        file1.write(text_editor)
        file1.close()

class EditorConigurator:
    def __init__(self, text):
        self.text = text
    
    # ação para alterar fonte do editor
    def fontCourier(self):
        self.text.config(font="Courier")

    # ação para alterar fonte do editor
    def fontHelvetica(self):
        self.text.config(font="Helvetica")