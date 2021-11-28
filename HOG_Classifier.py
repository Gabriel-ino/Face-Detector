import dlib
import cv2


class HOGClassifier:
    """
    A classifier object using HOG method with dlib library
    """
    def __init__(self, img):
        self.classifier = dlib.get_frontal_face_detector()
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



