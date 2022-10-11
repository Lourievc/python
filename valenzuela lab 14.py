#Lourie Valenzuela Cano
import os

iPath = "%homepath%\\Pictures\\"
aPath = "%homepath%\\Music\\"

print("Please, save your image file (zophie.jpg) inside your *Pictures* folder, and your audio file (Scots Wha Hae.mp3) inside your *Music* folder.")

song = input('Please type the audio file: ')
cmd = ("\"" + aPath + song + "\"")
os.system("\"" + cmd + "\"")

image = input('Please type the image file: ')
cmd = ("\"" + iPath + image + "\"")
os.system("\"" + cmd + "\"")

