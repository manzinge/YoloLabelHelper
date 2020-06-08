from matplotlib import image, patches, pyplot as plt
from matplotlib.widgets import Button

decision ={} 

def _yes(event):
    if event.button == 1:
        decision['dec'] = 1
        plt.close()
def _no(event):
    if event.button == 1:
        decision['dec'] = 2
        plt.close()
def _trash(event):
    if event.button == 1:
        decision['dec'] = 3
        plt.close()


def createPlot(img):
    plt.imshow(img)
    yescut = plt.axes([0.4, 0.0, 0.1, 0.095])
    nocut = plt.axes([0.6, 0.0, 0.1, 0.095])
    trashcut = plt.axes([0.9, 0.0, 0.1, 0.095])
    bcutyes = Button(yescut, 'YES', color='green', hovercolor='green')
    bcutno = Button(nocut, 'NO', color='red', hovercolor='red')
    bcuttrash = Button(trashcut, 'TRASH', color='BROWN', hovercolor='BROWN')
    bcutyes.on_clicked(_yes)
    bcutno.on_clicked(_no)
    bcuttrash.on_clicked(_trash)
    plt.show()