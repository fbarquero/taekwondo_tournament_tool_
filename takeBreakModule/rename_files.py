__author__ = 'Mordigan'
import os

def rename_file():
    path = r"E:\prank\prank"
    #get file names from folder
    file_list = os.listdir(path)
    print file_list
    os.chdir(path)
    for file in file_list:
        os.rename(file, file.translate(None, "123456789"))
    #for each file rename

rename_file()
