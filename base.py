import os


def get_path():
    file_path = os.path.abspath(__file__)
    return os.path.dirname(file_path)
