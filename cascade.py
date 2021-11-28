"""
    @Author: Gabriel Chaves Martins
    @Resume: A multiprocessing algorithm who identifies faces in images using different methods, the main
    idea is to compare the methods and see how it's the most effective depending on the image. In this case,
    we're detecting only faces, but you can use the other preprocessed results in this project to detect other
    things like cars, keys or clocks
"""

from my_utils import cleaning_terminal
from preprocessing import preprocessing
from Cascade_Classifier import DetectorHaarcascade, EyeDetector
from draw_rectangle import draw_rectangle
from pathlib import Path
from typing import Final
from multiprocessing import Process
from time import sleep

IMAGES_PATH: Final = str(Path(__file__).parent.resolve()) + '/training_images/Images'


def face_recognizer(face_detector: DetectorHaarcascade, eye_detector: EyeDetector, img_str: str, resize: bool):
    """
    This function will make the face recognition and the eye recognition
    :param face_detector: Face detector object
    :param eye_detector: Eye detector object
    :param img_str: image name
    :param resize: This param will define if the image will be resized or not
    :return: None
    """

    gray_scale, image = preprocessing(IMAGES_PATH + img_str, resize)
    face_detector.detecting(gray_scale)
    eye_detector.detecting(gray_scale)
    draw_rectangle(image, face_detector.detection, eyes_coordinates=eye_detector.detection)


def main():
    while True:  # The user will define how many images it'll be passed
        cleaning_terminal()
        sleep(0.2)
        add = input('Add an image? [Y/N] ').strip().upper()
        if add == 'Y':  # A new process will be created every time that the user selects the 'Y' option
            img_name = input("Type the image name: ").strip()
            resize = input("Resize? [Y/N] ").strip().upper()

            if resize == 'Y':
                resize = True
            else:
                resize = False

            print("Face detector: ")
            face_detector = DetectorHaarcascade(classifier='haarcascade_frontalface_default.xml')  # Preprocessing results to detect faces
            print("\n\nEye detector:")
            eye_detector = EyeDetector("haarcascade_eye.xml")  # Preprocessing results to detect eyes

            cleaning_terminal()  # Cleaning the terminal
            new_process = Process(target=face_recognizer, args=(face_detector, eye_detector, img_name, resize))  # Creating process object
            new_process.start()  # starting process

        elif add == 'N':
            break

    print("Bye")


if __name__ == "__main__":
    main()
