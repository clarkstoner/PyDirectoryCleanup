import configparser
import pathlib

config_file = configparser.ConfigParser()

config_file.add_section("source_dir")

source_dir = str(input("Enter Directory to watch - windows use \\\\ for file path, use / for any other machine: "))
print(source_dir)

config_file.set("source_dir", "directory_to_watch", source_dir)

config_file.add_section("move_to_id")
config_file.set("move_to_id", "1", "videos")
config_file.set("move_to_id", "2", "music")
config_file.set("move_to_id", "3", "picture")

config_file.add_section("move_to_dir")
config_file.set("move_to_dir", "1", "directory/to/move/items/to")
config_file.set("move_to_dir", "2", "directory/to/move/items/to")
config_file.set("move_to_dir", "3", "directory/to/move/items/to")

config_file.add_section("move_to_types")
config_file.set("move_to_types", "1", "['.mp4','.mkv']")
config_file.set("move_to_types", "2", "['.mp3']")
config_file.set("move_to_types", "3", "['.jpg','.png']")

with open(r"./conf.ini", 'w') as config_file_obj:
    config_file.write(config_file_obj)
    config_file_obj.flush()
    config_file_obj.close()

print(f"Config file 'conf.ini' created in {pathlib.Path(__file__).parent.parent.resolve()}")
print("Please go to file to finish setting up directorys and file extension to watch for. for more info please refer back to the github.")