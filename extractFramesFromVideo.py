import cv2
import os
import glob
import configparser
def getVideosFromDirectory(videoPath):
    video_list =[]
    for filename in glob.glob(videoPath + '/*.mp4'):
        video_list.append(filename) 
    return video_list

def checkFolders():
    if not os.path.exists('videoFrames'):
        os.makedirs('videoFrames')

def getConfigSettings():
    Config = configparser.ConfigParser()
    Config.read('config.ini')
    return Config.get("YOLO", 'videoPath')

def main():
    videoPath = getConfigSettings()
    checkFolders()
    videoList = getVideosFromDirectory(videoPath)
    for video in videoList:
        print("Working on Video:{}".format(video))
        videoPath = video
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
                imgName = os.getcwd() + '/videoFrames/' + videoName + '_' + str(i)+'.jpg'
                cv2.imwrite(imgName,frame)
                i+=1
            framecounter += 1
        
        cap.release()
        cv2.destroyAllWindows()


main()