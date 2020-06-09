import cv2
import os

videoPath = ''
videoNameExt = videoPath.split('/')[-1]
videoName = videoNameExt.split('.')[0]
cap= cv2.VideoCapture(videoPath)
i=0
framecounter = 1

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if framecounter % 5 == 0:
        imgName = os.getcwd() + '/VideoFrames/' + videoName + '_' + str(i)+'.jpg'
        cv2.imwrite(imgName,frame)
        i+=1
    framecounter += 1
 
cap.release()
cv2.destroyAllWindows()
