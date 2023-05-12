import os

class FileTypesInFolder:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def get_file_types(self):
        file_types = {}
        self._get_file_types_recursive(self.folder_path, file_types)
        return file_types

    def _get_file_types_recursive(self, folder_path, file_types):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(file_name)[1][1:].lower()
                if file_extension not in file_types:
                    file_types[file_extension] = []
                file_types[file_extension].append(file_path)
            elif os.path.isdir(file_path):
                self._get_file_types_recursive(file_path, file_types)
