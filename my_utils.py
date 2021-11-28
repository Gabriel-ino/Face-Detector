import os
import platform


def cleaning_terminal():
    """
    This function will clean the terminal of your computer to maintain organization in the processing, in Windows or
    Linux.
    :return: None
    """
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')







