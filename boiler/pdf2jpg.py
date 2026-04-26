import wand
import os
from wand.image import Image


# function to extract images from all pdfs in a given path
def pdfToImage(path_main):
    paths = os.listdir(path_main)
    try:
        os.mkdir(path_main + '/' + "output")
    except:
        pass
    y = 0
    for x in paths:
        if x[-4:] != ".pdf" and x[-4:] != ".PDF":
            continue
        path = path_main + "/" + x

        with Image(filename=path, resolution=100) as img:
            img.format = 'jpg'
            img.compression_quality = 0
            img.save(filename=path_main + "/" + "output" + "/airheater."+ str(y) + ".jpg")
        y += 1


# path in which pdf are located
path = "C:/Users/3019/machinelearning/boiler/airheater"
pdfToImage(path)
