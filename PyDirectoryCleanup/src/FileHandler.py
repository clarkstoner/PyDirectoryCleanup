from genericpath import exists
from watchdog.events import LoggingEventHandler
from PyDirectoryCleanup.src.FileMover import FileMover
import configparser
import ast
import os

config_file = configparser.ConfigParser()
config_file.read("./conf.ini")

source_dir = config_file["source_dir"]["directory_to_watch"]


class FileHandler(LoggingEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as items:
            for item in items:
                name = item.name
                dest = source_dir
                for move_type in config_file["move_to_id"]:
                    if name.endswith(tuple(ast.literal_eval(config_file["move_to_types"][str(move_type)]))):
                        dest = config_file["move_to_dir"][str(move_type)]
                        FileMover.move_file_to_new_dest(dest, item, name)