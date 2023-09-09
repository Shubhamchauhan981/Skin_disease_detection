from skimage.io import imread, imshow
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
from PIL import Image
import os,sys
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
from sklearn import svm, metrics, datasets
from sklearn.utils import Bunch
from sklearn.model_selection import GridSearchCV, train_test_split
import skimage

path=r'C:/Users/Subham/Downloads/Skin disease/Skin/mdenode_resized/'

dirs=os.listdir(path)

def save_hog():
    for item in dirs:
        for img in os.listdir(path+item):
            if os.path.isfile(path+item+'/'+img):
                a=path+'/'+item
                im=Image.open(path+item+'/'+img)
                im=np.array(im)
                img_eq=exposure.equalize_hist(im)
                f,e=os.path.splitext(img)
                fd, hog_image = hog(img_eq, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True, multichannel=True)
                hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10)) 
                plt.imsave(a+f + '_hog.jpg', hog_image_rescaled, cmap='Greys')

save_hog()