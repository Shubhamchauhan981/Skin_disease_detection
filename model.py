from PIL import Image
import os,sys
import matplotlib.pyplot as plt
import numpy as np
import skimage
from pathlib import Path
from skimage.io import imread
from sklearn.utils import Bunch
from sklearn import svm,metrics,datasets
from sklearn.model_selection import GridSearchCV,train_test_split
import pickle

def load_image(path):
        image_dir=Path(path)
        folders=[directory for directory in image_dir.iterdir() if directory.is_dir()]
        categories=[fo.name for fo in folders]
        images=[]
        flat_data=[]
        target=[]
        for i,direc in enumerate(folders):
            for file in direc.iterdir():
                img=imread(file)
                flat_data.append(img.flatten())
                images.append(img)
                target.append(i)
        flat_data=np.array(flat_data)
        target=np.array(target)
        images=np.array(images)
        return Bunch(data=flat_data,target=target,target_names=categories)

image_dataset=load_image(r'C:/Users/Subham/Downloads/Skin disease/Skin/hog_dataset/')

image_dataset.target_names

image_dataset.target

x_train,x_test,y_train,y_test=train_test_split(image_dataset.data,image_dataset.target,test_size=0.1)

model=svm.SVC()
model.fit(x_train,y_train)
pickle.dump(model,open('./svm.pkl','wb'))
pred=model.predict(x_test)
pred

from sklearn.metrics import accuracy_score
print(accuracy_score(pred,y_test))

from sklearn.naive_bayes import GaussianNB 

gnb = GaussianNB().fit(x_train, y_train) 
pickle.dump(gnb,open('./naive_bayes.pkl','wb'))
gnb_predictions = gnb.predict(x_test) 

print(accuracy_score(gnb_predictions,y_test))

print(gnb_predictions)

print(y_test)