from PIL import Image
import os

class Compressor:
    config = None
    path = None
    def __init__(self,config):
        self.config = config

    # TODO: USE A BETTER WAY TO DETERMINE FOR EACH IMAGE WHAT WOULD BE THE PERFECT COMPRESSION
    def quality_range(self,file_size_kb):
        if file_size_kb <= 300:
            return 80
        elif file_size_kb <= 600:
            return 75
        elif file_size_kb <= 1200:
            return 70
        elif file_size_kb <= 2000:
            return 65
        elif file_size_kb <= 4000:
            return 60
        elif file_size_kb <= 7000:
            return 55
        else:
            return 50

    def getImg(self,path):
        if not os.path.exists(path):
            return None 
        try:
            image = Image.open(path)
            file_size_bytes = os.path.getsize(path)
            return  {
                    "format": image.format,
                    "size": file_size_bytes,
                    }
        except:
            return None

    def assembleCompression(self, imgInfo):
        if(imgInfo == None):
            return None
        kilobytes = imgInfo["size"] / 1024
        if imgInfo["format"] in self.config["convert"]:
            convert_to = self.config["convert"][imgInfo["format"]]
        else:
            convert_to = None
        if self.config["overwrite"] and convert_to == None :
            path = self.path
        elif self.config["overwrite"] and convert_to != None:
            directory, filename = os.path.split(self.path)
            name, extension = os.path.splitext(filename)
            extension = "." + convert_to.lower()
            new_filename = name + "-compressed" + extension
            path = os.path.join(directory, new_filename)
        else:
            directory, filename = os.path.split(self.path)
            name, extension = os.path.splitext(filename)
            if(convert_to != None):
                extension = "." + convert_to.lower()
            new_filename = name + "-compressed" + extension
            path = os.path.join(directory, new_filename)
            
        return {
            "quality":self.quality_range(kilobytes),
            "path":path
        }

    def compress(self,path):
        self.path = path
        compress = self.assembleCompression(self.getImg(path))
        if(compress == None):
            return None
        extension = os.path.splitext(path)[1]
        if(extension == ".webp"):
           return None
        else:
            quality = f"-quality {compress['quality']}"
        # TODO: use a better way to compress
        # NOTE: no matter what compression tool i use compressing webp results in bigger size ! so just ignore for now 
        toPath = compress['path']
        cpath = f'"{path}"'
        toPath = f'"{toPath}"'
        os.system(f"convert {cpath} {quality} {toPath}")
        if path != compress['path']:
            os.remove(path)
        return compress['path']