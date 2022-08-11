from PyDirectoryCleanup.src.UniqueFileRename import UniqueFileRename
import os
import shutil

class FileMover():
    def move_file_to_new_dest(dest, item, name):
        if os.path.exists(f"{dest}/{name}"):
            unique_name = UniqueFileRename.make_unique_filename(dest, name)
            old_name = os.path.join(dest, name)
            new_name = os.path.join(dest, unique_name)
            os.rename(old_name, new_name)
        shutil.move(item, dest)