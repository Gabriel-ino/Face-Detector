import cv2
from pathlib import Path
from typing import Final
from HOG_Classifier import HOGClassifier

FILE_PATH: Final = str(Path(__file__).parent.resolve()) + '/training_images/Images'  # The directory of the images


def HOG_implement():
    """
    Implementing HOG method with dlib, the HOG classifier tends to be better results than Cascade method,
    it works using derivatives that percepts the degree of change
    :return:
    """
    img_str = input("Type the image name: ").strip()

    img = cv2.imread(FILE_PATH + img_str)
    print(img)
    hog = HOGClassifier(img)

    while True:
        hog.detecting(img)
        key = cv2.waitKey(1)









