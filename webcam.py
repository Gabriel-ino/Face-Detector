import cv2
import sys
from os import execl


def showing_webcam(**kwargs):
    """
    In this method you'll pass the model of face detector to detect a face in the images that your webcam
    will show
    :param kwargs: model face detector
    :return: None
    """
    video = cv2.VideoCapture(0)
    model = kwargs.get('model')

    while True:
        _, frame = video.read()
        detector = model(img=frame)
        detector.detecting(frame)

        cv2.waitKey(1)


try:
    choose = int(input("Model\n1-Cascade\n2-HOG\n3-CNN"))

except Exception as err:
    print("Please type a valid value")
    execl(sys.executable, sys.executable, *sys.argv)  # This function will reinitialize the program

if choose == 1:
    from Cascade_Classifier import DetectorHaarcascade
    showing_webcam(model=DetectorHaarcascade)

elif choose == 2:
    from HOG_Classifier import HOGClassifier
    showing_webcam(model=HOGClassifier)

elif choose == 3:
    from CNN_Classifier import CNNClassifier
    showing_webcam(model=CNNClassifier)
