from matplotlib import image, pyplot as plt
from pythonAnalyser import analyseImage
from createPlot import createPlot
from createPlot import decision
import glob
import cv2
import shutil

labelsPath = ''
weightsPath = ''
configPath = ''
imgPath = ''

def getImagesFromDirectory():
    image_list = []
    for filename in glob.glob(imgPath + '/*.jpg'):
        image_list.append(filename)
    return image_list

def main():
    imgList = getImagesFromDirectory()
    counter = 1
    for img in imgList:
        print("You are working on {} of {}".format(counter, len(imgList)))
        boxes, image = analyseImage(labelsPath, weightsPath, configPath, img)
        createPlot(image)
        imgArray = img.split('/')
        cut = imgArray[:len(imgArray)-2]
        if decision['dec'] == 1:
            labelFileName = "trainImages/" + img.split('/')[-1].split('.')[0] + ".txt"
            labelFile = open(labelFileName, 'a')
            for detection in boxes:
                labelFile.write("0 {} {} {} {} \n".format( \
                    detection[0] / 1000, \
                    detection[1] / 1000, \
                    detection[2] / 1000, \
                    detection[3] / 1000)
                )

            labelFile.close()
            movePath = '/'.join(cut) + '/trainImages/' + imgArray[-1].split('.')[0] + ".jpg"

        elif decision['dec'] == 2:
            movePath = '/'.join(cut) + '/reLabel/' + imgArray[-1].split('.')[0] + ".jpg"

        elif decision['dec'] == 3:
            movePath = '/'.join(cut) + '/trashImages/' + imgArray[-1].split('.')[0] + ".jpg"
        
        shutil.move(img,movePath)
        counter += 1

main()