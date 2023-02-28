import os
import json

def returnFiles(foldername):
    with open(foldername) as f:
        d = json.load(f)
        for elem in d:
            if(elem["device_ids"]!=[]):
                print(foldername)
                

filename=r"C:\Users\sesa650375\Downloads\ProcessedFiles"
for folder1 in os.listdir(filename):
    for folder2 in os.listdir(filename+"\\"+folder1):
        for folder3 in os.listdir(filename+"\\"+folder1+"\\"+folder2+"\\output"):
            if(folder3.endswith("dc.json") or folder3.endswith("dd.json")):
                returnFiles(filename+"\\"+folder1+"\\"+folder2+"\\output"+"\\"+folder3)



