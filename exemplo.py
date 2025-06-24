from abc import ABC, abstractmethod

# Componente base
class FileSystemComponent(ABC):
    @abstractmethod
    def show(self, indent=0):
        pass

# Folha
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print(" " * indent + f"Arquivo: {self.name}")

# Composite
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def show(self, indent=0):
        print(" " * indent + f"Pasta: {self.name}")
        for child in self.children:
            child.show(indent + 2)

# Uso
root = Folder("raiz")
root.add(File("arquivo1.txt"))
root.add(File("arquivo2.txt"))

sub_folder = Folder("documentos")
sub_folder.add(File("curriculo.pdf"))
sub_folder.add(File("relatorio.docx"))

root.add(sub_folder)

root.show()