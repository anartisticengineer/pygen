import sys
import os
import utils.fileutils as util
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
            util.makeAndChangeToDirectory(destFolderName)
            # create startup files
            util.createFile("LICENSE.md")
            util.createFile("README.md")
            util.createFile(".gitignore")
            # create another directory level to store the main py file
            util.makeAndChangeToDirectory(destFolderName)
            util.createFile("__main__.py")
        print("Done ~ ^.^")
        print("You can peep the file here:")
        os.chdir("../")
        print(os.getcwd())
