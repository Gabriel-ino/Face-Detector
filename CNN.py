import cv2
from pathlib import Path
from typing import Final
from CNN_Classifier import CNNClassifier


FILE_PATH: Final = str(Path(__file__).parent.resolve()) + '/training_images/Images'  # The directory of the images


def CNN():
    img_str = input("Type the image name: ").strip()
    img = cv2.imread(FILE_PATH + img_str)
    cnn = CNNClassifier(img)

    while True:
        cnn.detecting(img)
        key = cv2.waitKey(1)

