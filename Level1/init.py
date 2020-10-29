from os import path

def get_file(fileName):
    """
    Returns the absolute path of a file
    """
    #This grabs your files from your folder
    return path.join(path.dirname(__file__), fileName)
