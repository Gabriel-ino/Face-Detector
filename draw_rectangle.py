import cv2
from time import sleep


def draw_rectangle(image, coordinates, **kwargs):
    """
    This function will draw a rectangle in the original image, in the coordinates who will be passed
    :param image: image's matrix
    :param coordinates: matrix with the X & Y coordinates, and the width & height to the size of the face
    :return:
    """
    for x, y, w, h in coordinates:  # getting x,y,w,h coordinates in the passed matrix, where x & y are the coordinates and
        # w & h are the size of the face, in pixels
        print((w, h))  # Showing the size of the faces
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)

    try:
        eyes_coordinates = kwargs.get('eyes_coordinates')

        for x,y,w,h in eyes_coordinates:
            print((w, h))
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    except Exception as err:
        pass

    sleep(0.2)

    while True:
        cv2.imshow('detector', image)
        cv2.waitKey(1)




