from matplotlib import image, pyplot as plt
from pythonAnalyser import analyseImage
from createPlot import createPlot
from createPlot import decision
import cv2
import os
import glob
import cv2
import shutil
import configparser
def getImagesFromDirectory(imgPath):
    image_list = []
    for filename in glob.glob(imgPath + '/*.jpg'):
        image_list.append(filename)
    return image_list

def checkFolders():
    if not os.path.exists('reLabel'):
        os.makedirs('reLabel')
    if not os.path.exists('trainImages'):
        os.makedirs('trainImages')
    if not os.path.exists('trashImages'):
        os.makedirs('trashImages')

def getConfigSettings():
    Config = configparser.ConfigParser()
    Config.read('config.ini')
    return Config.get("YOLO", 'labelsPath'), Config.get("YOLO", 'weightsPath'), Config.get("YOLO", 'configPath') ,Config.get("YOLO", 'imgPath')

def saveLabelFile(img, boxes, w, h, path):
    labelFileName = path + img.split('/')[-1].split('.')[0] + ".txt"
    labelFile = open(labelFileName, 'a')
    for detection in boxes:
        x = detection[0] / w
        y = detection[1] / h
        length = detection[2] / w
        height = detection[3] / h
        labelFile.write("0 {} {} {} {} \n".format(x, y, length, height))

    labelFile.close()


def main():
    labelsPath, weightsPath,configPath, imgPath = getConfigSettings()
    checkFolders()
    imgList = getImagesFromDirectory(imgPath)
    counter = 1
    for img in imgList:
        print("You are working on {} of {}".format(counter, len(imgList)))
        im = cv2.imread(img)
        h, w, c = im.shape
        boxes, image = analyseImage(labelsPath, weightsPath, configPath, img)
        createPlot(image)
        imgArray = img.split('/')
        cut = imgArray[:len(imgArray)-2]
        if decision['dec'] == 1:
            saveLabelFile(img,boxes,w,h, 'trainImages/')
            movePath = '/'.join(cut) + '/trainImages/' + imgArray[-1].split('.')[0] + ".jpg"

        elif decision['dec'] == 2:
            saveLabelFile(img,boxes,w,h, 'reLabel/')
            movePath = '/'.join(cut) + '/reLabel/' + imgArray[-1].split('.')[0] + ".jpg"

        elif decision['dec'] == 3:
            movePath = '/'.join(cut) + '/trashImages/' + imgArray[-1].split('.')[0] + ".jpg"
        
        shutil.move(img,movePath)
        counter += 1

main()