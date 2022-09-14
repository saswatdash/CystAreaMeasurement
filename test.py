'''
Draw a reference circle whose diameter is 22 micrometer on the left top corner of the image.
'''

import cv2
import os
import re
import fnmatch

cwd = os.getcwd()
my_list = []

#Draw a circle with 
for subdir, dirs, files in os.walk(cwd, topdown=True):
    del dirs[:]  # remove the sub directories.
    for file in files:
        if not(re.search("py",file)):
           image = cv2.imread(file)
           cv2.circle(image,center=(100,100),radius=71,color=(255,0,0),thickness=2)
           cv2.imwrite(file+'.tif',image)
