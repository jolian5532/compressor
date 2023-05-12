from compressor import Compressor
from folder_sort import FileTypesInFolder

imgExts = ["jpg","png","webp", "jpeg"]
config = {"convert":{"PNG":"WEBP"},"overwrite":True}
hello = Compressor(config)  

folder = '../a/'
file_types_in_folder = FileTypesInFolder(folder)
files = file_types_in_folder.get_file_types()

for file_type, files in files.items():
    if file_type in imgExts:
        for file in files:
            print(hello.compress(file))
