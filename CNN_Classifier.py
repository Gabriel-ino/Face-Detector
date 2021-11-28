import cv2
import dlib


class CNNClassifier:
    def __init__(self, img):
        self.classifier = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')
        self.detector = self.classifier(img, 1)  # Scale

    def detecting(self, img):
        """
        This function will take the image's array and then draw a rectangle in faces positions
        :param img: image array
        :return: None
        """
        for val in self.detector:
            left, right, top, bottom = val.left(), val.right(), val.top(), val.bottom()
            cv2.rectangle(img, (left, top), (right, bottom), (255, 0, 0), 2)

        cv2.imshow("Detecting...", img)



