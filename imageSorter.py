
# Pythono3 code to sort images in folders

from PIL import Image
from PIL import ExifTags
# importing os module and math
import os
import math

# Function to sort multiple images based on creation date
def main():
    directory = input("enter the directory of unsorted images:")
    for images in os.listdir(directory):
        print(images)
        if images.endswith('.jpg') or images.endswith('.jpg'):
        name = images.split(".")
        if len(name)==2:
            if (name[1]=='.jpg' or name[1]=='.jpeg':
                img = Image.open(images)
                exifDataRaw = img._getexif()
                for tag, value in exifDataRaw.items():
                    decodedTag = ExifTags.TAGS.get(tag, tag)
                    exifData[decodedTag] = value
                print(exifDataRaw)

                # dst =name[2] + "." + name[1] + "." + name[0]
                # src = directory + "\\" + folders
                # dst = directory + "\\" + dst

                # rename() function will
                # rename all the files
                # os.rename(src, dst)

# Driver Code
if __name__ == '__main__':

	# Calling main() function
	main()
