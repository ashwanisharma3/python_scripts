#Author: Ashwani
#Description: This script organize file according to their type in folders of similar type.


import os, sys, shutil

def makeFolders(directory,fileTypes):
    for i in fileTypes:
        dir= directory + "\\" + i
        if not os.path.exists(dir):
            os.mkdir(dir)

def move(directory, filename, fileTypes):
    if "." in filename:
        fileFormat = filename.split(".")
        ext = fileFormat[-1]
    else:
        print (filename + " has not been moved.")
        return

    for filetype in fileTypes.keys():
        if ext in fileTypes[filetype]:
            src = directory + "\\" + filename
            dst = directory + "\\" + filetype + "\\" + filename
            shutil.move(src, dst)
            #print (shutil.move(src, dst))

def removeEmptyDir(directory):
    for folder in os.listdir(directory):
        if not len(os.listdir(directory+"\\"+folder)):
            os.rmdir(directory+"\\"+folder)

def main():

    #folders' name of types of files they will having according to extension they have
    fileTypes = {}
    fileTypes["Images"] = ["jpg", "gif", "png", "jpeg", "bmp"]
    fileTypes["Audio"] = ["mp3", "wav", "aiff", "flac", "aac"]
    fileTypes["Video"] = ["m4v", "flv", "mpeg", "mov", "mpg", "mpe", "wmv", "MOV", "mp4"]
    print("For classification in docs only press 1 else for classification into Excel, Docs, Pdf, etc press 0")
    x=int()
    x=input()
    if x==1:
    	fileTypes["Documents"] = ["doc", "docx", "txt", "ppt", "pptx", "pdf", "rtf", "xlsx", "csv"]
    else:
    	fileTypes["Docs"] = ["doc", "docx", "rtf", "txt"]
    	fileTypes["Powerpoint"] = ["ppt", "pptx"]
    	fileTypes["Pdf"] = ["pdf"]
    	fileTypes["Excel"] = ["xlsx", "csv"]
    fileTypes["Exe"] = ["exe"]
    fileTypes["Compressed"] = ["zip", "tar", "7", "rar"]
    fileTypes["Virtual_Machine_and_iso"] = ["vmdk", "ova", "iso"]
    fileTypes["Programs"] = ["java", "py", "c", "cpp", "sql"]
    fileTypes["Shortcuts"] = ["lnk"]
    print("Enter the location")
    directory = input()
    files = os.listdir(directory)
    makeFolders(directory,fileTypes)
    for file in files:
        move(directory, file, fileTypes)
    removeEmptyDir(directory)



main()
