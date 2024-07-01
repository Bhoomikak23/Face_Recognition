from os import listdir  
import cv2   
import numpy as np  

root_dir = "./dataset" 

features = []  
labels = []  

i = 0   
for subfolder in listdir(root_dir):   
    path = f"{root_dir}/{subfolder}"   
    print(f"------------------{path}-----------------")   
   
    for file in listdir(path): 
        filepath = f"{path}/{file}" 
        image = cv2.imread(filepath, 0)  
        features.append(image)   
        labels.append(i)  
    
    i += 1   

print(f"length of features = {len(features)}")
print(f"length of labels = {len(labels)}")   

recog = cv2.face.LBPHFaceRecognizer_create()


recog.train(features, np.array(labels))


recog.save("facemodel.yml")



