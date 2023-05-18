from compressor import Compressor
from folder_sort import FileTypesInFolder
from file_compress import ffile
import os 

imgExts = ["jpg","png", "jpeg"]
imgs = []
convert = {"PNG":"WEBP"}
folder = '../a/'

file_types_in_folder = FileTypesInFolder(folder)
files = file_types_in_folder.get_file_types()
for file_type, files in files.items():
    if file_type.upper() in convert:
        for file in files:
            imgs.append(os.path.basename(file))

config = {"convert":convert,"imgs":imgs,"overwrite":True}

compress = ffile(config)
img = Compressor(config)      

file_types_in_folder = FileTypesInFolder(folder)
files = file_types_in_folder.get_file_types()
for file_type, files in files.items():
    if file_type in imgExts:
        count = 0
        length = len(files)
        for file in files:
            img.compress(file)
            count = count + 1 
            print(f"{file_type.upper()} : {count}/{length}")
    if file_type == "html":
        length = len(files)
        count = 0
        for file in files:
            compress.html(file)
            count = count + 1 
            print(f"HTML : {count}/{length}")
    if file_type == "css":
        length = len(files)
        count = 0
        for file in files:
            compress.css(file)
            count = count + 1 
            print(f"CSS : {count}/{length}")
    if file_type == "js":
        length = len(files)
        count = 0
        for file in files:
            compress.js(file)
            count = count + 1 
           # print(f"JS : {count}/{length}")
