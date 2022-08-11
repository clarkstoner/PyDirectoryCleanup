from genericpath import exists
from watchdog.events import LoggingEventHandler
from PyDirectoryCleanup.src.FileMover import FileMover
import configparser
import os

config_file = configparser.ConfigParser()
config_file.read("./conf.ini")

source_dir = config_file["source_dir"]["directory_to_watch"]
dest_dir_videos = config_file["source_dir"]["directory_to_watch"]
dest_dir_images = config_file["source_dir"]["directory_to_watch"]

class FileHandler(LoggingEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as items:
            for item in items:
                name = item.name
                dest = source_dir
                if name.endswith(".jpg") or name.endswith(".png"):
                    dest = dest_dir_images
                    FileMover.move_file_to_new_dest(dest, item, name)
                elif name.endswith(".mov") or name.endswith(".mp4") or name.endswith(".mkv"):
                    dest = dest_dir_videos
                    FileMover.move_file_to_new_dest(dest, item, name)