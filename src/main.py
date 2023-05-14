from compressor import Compressor
from folder_sort import FileTypesInFolder
from file_compress import file

imgExts = ["jpg","png", "jpeg"]
config = {"convert":{"PNG":"WEBP"},"overwrite":True}
hello = Compressor(config)      
compress = file(config)
folder = '../a/'
file_types_in_folder = FileTypesInFolder(folder)
files = file_types_in_folder.get_file_types()

for file_type, files in files.items():
    if file_type in imgExts:
        length = len(files)
        count = 0
        for file in files:
            hello.compress(file)
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
            print(f"JS : {count}/{length}")
