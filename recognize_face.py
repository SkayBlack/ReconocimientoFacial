import cv2,os
import numpy as np
import pickle
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# path = "C:/Users/FX/pythonProjects/face-recognition-and-tts-numbers/trainner/"

def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]

    for imagePath in imagePaths:
        print('e-> '+imagePath)

    # exit()
    faceSamples=[]
    Ids=[]
    Names=[]
    index = 0
    for (subdirs, dirs_users, files) in os.walk(path):
        for user_path in dirs_users:
            Names.append(user_path)
            subjectpath = os.path.join(path, user_path)
            for filename in os.listdir(subjectpath):
                imagePath = subjectpath + '/' + filename
                # images.append(cv2.imread(path, 0))
                # lables.append(int(lable))
                pilImage = Image.open(imagePath).convert('L')
                imageNp = np.array(pilImage,'uint8')
                faces = detector.detectMultiScale(imageNp)
                for (x,y,w,h) in faces:
                    faceSamples.append(imageNp[y:y+h,x:x+w])
                    Ids.append(int(index))
            index += 1

    return faceSamples,Ids,Names

def run():
    faces,Ids,Names = getImagesAndLabels('dataSet')
    with open("names.pickle","wb") as f:
        pickle.dump(Names,f)
    
    recognizer.train(faces, np.array(Ids))
    recognizer.write('trainner/trainner.yml')

# run()
