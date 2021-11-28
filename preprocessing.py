import cv2


def preprocessing(img_path: str, resizing=True):
    """
    This function will preprocess the images, turning them on gray scale and resizing them for better processing
    :param: Image path
    :return: Preprocessed image
    """
    img = cv2.imread(img_path)
    print(img.shape)
    if resizing:
        img = cv2.resize(img, (800, 600))  # Resizing image to 800x600 px

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converting RGB to Grey image, to take less time for
    # processing image
    gray_image.shape

    return gray_image, img



