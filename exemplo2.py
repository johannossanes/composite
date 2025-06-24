class File:
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print(" " * indent + f"Arquivo: {self.name}")

class Folder:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.folders = []

    def add_file(self, file):
        self.files.append(file)

    def add_folder(self, folder):
        self.folders.append(folder)

    def show(self, indent=0):
        print(" " * indent + f"Pasta: {self.name}")
        for file in self.files:
            file.show(indent + 2)
        for folder in self.folders:
            folder.show(indent + 2)

# Uso
root = Folder("raiz")
root.add_file(File("arquivo1.txt"))
root.add_file(File("arquivo2.txt"))

sub_folder = Folder("documentos")
sub_folder.add_file(File("curriculo.pdf"))
sub_folder.add_file(File("relatorio.docx"))

root.add_folder(sub_folder)

root.show()