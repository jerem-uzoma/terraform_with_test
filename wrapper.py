# Import the OS and subprocess module
import subprocess
import os

# get the current working directory (this should be the root folder of the terrform repo)
rootdir = os.getcwd()

# we can iterate through the terraform repo folders and look for folders with a go test file 
for subdir, dirs, files in os.walk(rootdir):
    for dir in dirs:
        # change directory to the current directory
        os.chdir(dir)
        try:
            subprocess.Popen(["go", "test", "-v", "-timeout", "30m"])
        except FileNotFoundError:
            print("No terratest file in this directory: {0}".format(dir))
        except NotADirectoryError:
            print("{0} is not a directory".format(dir))
        except PermissionError:
            print("You do not have permissions to access {0}".format(dir))
