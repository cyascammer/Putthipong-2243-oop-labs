'''
Putthipong Phukhansung
633040224-3
Problem 2
'''
from abc import ABC, abstractmethod
 
class Image(ABC):

    @abstractmethod
    def load_image(self, name):
        pass
 
    def save_image(self, name):
        pass
 
class Bitmap(Image):
    def load_image(self, name):
        print(f"loading bitmap file {name}")

    def save_image(self, name):
        print(f"saving bitmap file {name}")
 
class Jpeg(Image):
    def load_image(self, name):
        print(f"loading bitmap file {name}")

    def save_image(self, name):
        print(f"saving bitmap file {name}")


if __name__ == '__main__':
    bitmap1 = Bitmap()
    bitmap1.save_image("kku.bmp")
    bitmap1.load_image("KKu.bmp")