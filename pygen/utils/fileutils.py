import os


def createFile(filename):
    f = open(filename, "w")
    f.close()
    del f


def makeAndChangeToDirectory(directoryName):
    os.mkdir(directoryName)
    os.chdir(directoryName)
