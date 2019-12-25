
# Pythono3 code to sort images in folders

from PIL import Image
from PIL import ExifTags
# importing os module and math
import os
import math
import shutil
from pathlib import Path

# Function to sort multiple images based on creation date
def main():
    directory = input("enter the directory of unsorted images:")
    for images in os.listdir(directory):
        print(images)
        if images.endswith('.JPG') or images.endswith('.jpg') or images.endswith('.jpg'):
            # print("image found")
            name = images.split(".")
            if len(name)==2:
                # print("len(name)==2")
                # print(name)
                if name[1]=='jpg' or name[1]=='jpeg' or name[1]=='JPG':
                    exifData = {}
                    img = Image.open(directory + "\\" + images)
                    exifDataRaw = img._getexif()
                    for tag, value in exifDataRaw.items():
                        decodedTag = ExifTags.TAGS.get(tag, tag)
                        exifData[decodedTag] = value
                    # print(exifDataRaw)
                    creationDate = exifData["DateTime"]
                    # print(exifData["DateTime"])
                    folderNameList = creationDate.replace(' ', ':').split(":")
                    # print(folderNameList)
                    foldername = directory + "\\" + folderNameList[0] + "." + folderNameList[1] + "." + folderNameList[2] 
                    # print(foldername)
                    if not os.path.exists(foldername):
                        os.makedirs(foldername)
                    img.close()
                    # funktion shutil sollte auch funktionieren
                    # shutil.move(directory + "\\" + images, foldername + "\\" + images)
                    try:
                        Path(directory + "\\" + images).rename(foldername + "\\" + images)
                    except FileExistsError as e:
                        print(e)

# Driver Code
if __name__ == '__main__':

	# Calling main() function
	main()
