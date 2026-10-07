import subprocess
import os

path = input("enter input path: ")
path = path[1:-1]

if not os.path.exists(path):
    print("Path does not exist.")
    exit()

ext = input("enter desired format: ")

new = path

i=-1
while(new[i]!= '.'):
    i-=1

new = new[:i] + '.' + ext

subprocess.run(["magick", path, new])