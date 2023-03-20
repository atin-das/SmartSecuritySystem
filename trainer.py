import os
import cv2
import numpy as np
from PIL import Image
#from PIL.Image import core as _imaging


#recognizer=cv2.createLBPHFaceRecognizer();
recognizer=cv2.face.LBPHFaceRecognizer_create();
path='dataSet'

def getImagesWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L');
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    return np.array(IDs), faces


IDs,faces=getImagesWithID(path)
recognizer.train(faces,IDs)
recognizer.save('recognizer/trainingdata.yml')
cv2.destroyAllWindows()

        
    #print imagePaths

#getImagesWithID(path)
