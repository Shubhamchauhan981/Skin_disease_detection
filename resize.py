from PIL import Image
import os,sys

path=r'C:/Users/Subham/Downloads/Skin disease/Skin/mdenode_resized/'

dirs=os.listdir(path)
dirs

def resize():
    for item in dirs:
        for img in os.listdir(path+item):
            if os.path.isfile(path+item+'/'+img):
                a=path+'/'+item
                try:
                    im=Image.open(path+item+'/'+img)
                    f,e=os.path.splitext(img)
                    imResize = im.resize((128,64), Image.ANTIALIAS)
                    imResize.save(a+f + '_resized.jpg', 'JPEG', quality=90)
                except:
                    continue

resize()