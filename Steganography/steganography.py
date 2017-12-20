from stegano import lsb
from stegano import lsbset
from stegano.lsbset import generators
import os;

class Steganographer:
    def __init__(self):
        self.choices = {
            "Fibonacci": generators.fibonacci,
            "Eratosthenes": generators.eratosthenes,
            "Logarithm": generators.log_gen
        } #Choices for the generator sets

    def encodePng(self, path, string):
#        if ".png" not in path:
#            path = path + ".png"
#        if "./" not in path:
#            path = "./" + path

        newImage = lsb.hide(path, string)
        newImage.save("./Steganography/steganized/"+os.path.basename(path))

    def decodePng(self, path):
#        if "./" not in path:
#            path = "./" + path
        return lsb.reveal(path)
        #Returns string

    #Encodes string to img with a generator set
    def encodePngWithSet(self, path, string, choice=None):
#        if ".png" not in path:
#            path = path + ".png"
#        if choice is None:
#            choice = "Fibonacci"
#        if "./" not in path:
#            path = "./" + path
#        print(self.choices)
        print(choice)
        print(self.choices)
        newImage = lsbset.hide(path, string, self.choices[choice]())
        newImage.save("./Steganography/steganized/"+os.path.basename(path))
        print("Called!")

    #Decodes the string from the image made with a generator set
    def decodePngWithSet(self, path, choice):
#        if "./" not in path:
#            path = "./" + path
        message = lsbset.reveal(path, self.choices[choice]())
        return message
        #Returns string
##for testing
#steganographer = Steganographer()
#
##Basic Steganography with LSB(Least Significant Bit)
#steganographer.encodePng("wallpaper.png", "hello world")
#print(steganographer.decodePng("./steganized/wallpaper.png"))
#
##Use same set for encode and decode for program to decode properly
#steganographer.encodePngWithSet("wallpaper.png", "hindi mo ako kaya", "Eratosthenes")
#print(steganographer.decodePngWithSet("./steganized/wallpaper.png", "Eratosthenes"))
