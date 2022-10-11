from zipfile import ZipFile
import os

print('Enter the names of the files you would like to zip.')
file1 = input("Enter the first file's name: ")
file2 = input("Enter the second file's name: ")

print('Enter the name of the folder that you would like to zip.')
new_folder = str(input("Enter the name of the folder to zip: "))
os.system('mkdir {}'.format(new_folder))
os.system('move {} {}'.format(file1,new_folder))
os.system('move {} {}'.format(file2,new_folder))

zipped_filename = input("Enter the name that you would like the zipped file to be called: ")  
# Walk through the directory of new_folder and add the files to an archive
with ZipFile(zipped_filename, 'w') as zip:
   for path, directories, files in os.walk(new_folder):
       for file in files:
           file_name = os.path.join(path, file)
           zip.write(file_name) 
print("Contents of the zip file: ")
with ZipFile(file, 'r') as zip:
   zip.printdir()