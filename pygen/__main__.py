import sys
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    # get environment variables from .env file
    load_dotenv()
    destFolderName = sys.argv[1]
    destPathName = os.getenv("DEST_PATH")
    if destPathName == None:
        # tell the user to create a .env file (or something else went wrong)
        pass
    else:
        os.chdir(destPathName)
        if os.path.exists(destFolderName):
            pass
        else:
            # create and navigate to the new folder
            print("Creating new folder at " + os.getcwd())
            os.mkdir(destFolderName)
            os.chdir(destFolderName)
            # will be a separate function for creating files
            li = open("LICENSE.md", "w")
            li.close()
            del li
            readMe = open("README.md", "w")
            readMe.close()
            del readMe
            gitIgnore = open(".gitignore", "w")
            gitIgnore.close()
            del gitIgnore
            # create another directory level to store the main py file
            os.mkdir(destFolderName)
            os.chdir(destFolderName)
            mainPyFile = open("__main__.py", "w")
            mainPyFile.close()
            del mainPyFile
        print("Done ~ ^.^")
        print("You can peep the file here:")
        os.chdir("../")
        print(os.getcwd())
