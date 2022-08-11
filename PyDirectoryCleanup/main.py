from watchdog.observers import Observer
from src.FileHandler import FileHandler
import time
import logging
import configparser

config_file = configparser.ConfigParser()
config_file.read("./conf.ini")

source_dir = config_file["source_dir"]["directory_to_watch"]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%mcl-%d %H:%M:%S')
    path = source_dir
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()