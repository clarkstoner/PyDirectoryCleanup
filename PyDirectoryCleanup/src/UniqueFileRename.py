from genericpath import exists
import os

class UniqueFileRename():
    def make_unique_filename(dest, name):
        filename, extension = os.path.splitext(name)
        counter = 1
        while exists(f"{dest}/{name}"):
            name = f"{filename}({str(counter)}){extension}"
            counter += 1
        return name