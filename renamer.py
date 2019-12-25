# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os 
import math

# Function to rename multiple files 
def main(): 
    directory = input("enter the directory:")
    for folders in os.listdir(directory):
        print(folders)
        name = folders.split(".")
        if len(name)==3:
            if (name[0].isnumeric() and len(name[0])==2) and (name[1].isnumeric() and len(name[1])==2) and (name[2].isnumeric() and len(name[2])==4):
                dst =name[2] + "." + name[1] + "." + name[0]
                src = directory + "\\" + folders 
                dst = directory + "\\" + dst 
                
                # rename() function will 
                # rename all the files 
                os.rename(src, dst)

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 
