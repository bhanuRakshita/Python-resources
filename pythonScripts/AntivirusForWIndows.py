import os

# Path to the directory to be scanned
path = "C:\\Users\\User\\Desktop\\scan"

def scanDirectory(path): # function to scan the directory
    for root, dirs, files in os.walk(path): # looping through the directory
        for file in files: # looping through the files
            if file.endswith(".exe"): # checking if the file is an executable file
                fileLocation=os.path.join(root, file) # getting the location of the file
                os.remove(fileLocation) # deleting the file
                print("File Deleted: ", fileLocation) # printing the message if the file is deleted

scanDirectory(path) # calling the function