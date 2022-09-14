import numpy as np
import matplotlib.pyplot as plt
import cv2
import re
import os


cwd = os.getcwd()
my_list = []

for subdir, dirs, files in os.walk(cwd, topdown=True):
    del dirs[:]  # remove the sub directories.
    for file in files:
        if not(re.search("py",file)):
            my_list.append(file)

# print(my_list)

for file in my_list:
    cnt =1
    img = cv2.imread(file)
    # print (file)
    cv2.circle(img,center=(100,100),radius=66,color=(0,0,250),thickness=4)
    cv2.imwrite('file.tif',img)
    #plt.imshow(img)
    file = file.strip('.tif')
    plt.savefig(file+str(cnt)+'.tif')
