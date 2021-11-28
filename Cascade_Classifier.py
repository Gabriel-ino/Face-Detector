import cv2


class DetectorHaarcascade:
    """
    This class will use the cascade method to detect faces in a image, it'll receive the image's matrix and the
    scale factor by detecting_faces function call
    """

    def __init__(self, img='', classifier: str = 'haarcascade_frontalface_default.xml'):
        self.detector = cv2.CascadeClassifier(classifier)
        try:
            self.scaleFactor = float(input("Type the scale factor in float format: ").strip())
            self.minNeighbors = input("Type the min neighbours to the image o press Enter without anything: ").strip()
            if len(self.minNeighbors) == 0:  # Passing the default value if the user don't write anything
                self.minNeighbors = None

            else:
                self.minNeighbors = int(self.minNeighbors)

            self.minSize = (int(input("Type the min size X and Y or pass 0 in both\nX:")), int(input("Y: ")))
            self.maxSize = (int(input("Type the max size X and Y or pass 0 in both\nX:")), int(input("Y: ")))

            if self.minSize == (0, 0):
                self.minSize = None
            if self.maxSize == (0, 0):
                self.maxSize = None

        except Exception as err:
            print(f"Error: {err}\nProbably you didn't type a valid value")

    def detecting(self, image):
        self.detection = self.detector.detectMultiScale(image, scaleFactor=self.scaleFactor,
                                                        minNeighbors=self.minNeighbors,
                                                        minSize=self.minSize,
                                                        maxSize=self.maxSize
                                                        )  # Changing the default value in
        # scale factor, who is the variable that defines the scale of image and detect bigger or smaller faces in the
        # picture, to obtain better results. The minNeighbors argument will define how many neighbors an image have to
        # be for considering it an image

        for x,y,w,h in self.detection:
            print((w, h))  # Showing the size of the faces
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.imshow('detecting', image)


class EyeDetector(DetectorHaarcascade):
    """
    This class will identify an eye in the image using cascade method
    """

    def __init__(self, classifier):
        super().__init__(classifier=classifier)  # Inheritance saves lives!
