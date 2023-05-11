from compressor import Compressor

config = {"convert":{"PNG":"WEBP"},"overwrite":False}
hello = Compressor(config)  
print(hello.compress("hello.jpeg"))