import zipfile
import numpy
import magic
import sys
import os
from collections import defaultdict

lengthMap = defaultdict(int)

def processFile(file, openZip=None):
    if file.lower().endswith(".txt"):
        print('Found txt file: {}'.format(file))
        if (openZip):
            processTxt(openZip.open(file, 'r'))
        else:
            processTxt(open(file))
    elif file.lower().endswith(".zip"):
        print('Found zip file: {}'.format(file))
        processZip(file)
        print('Done with zip file: {}'.format(file))

def processZip(file):
    with zipfile.ZipFile(file, 'r') as openZip:
        for zippedFile in openZip.namelist():
            processFile(zippedFile, openZip)

def processTxt(file):
    for line in file:
        for word in line.split():
            print(len(word))
            lengthMap[len(word)] += 1

def processDirectory(dir):
    if (os.path.isdir(dir)):
        for root, dirs, files in os.walk(dir):
            for file in files:
                processFile(os.path.join(root, file))
    else:
        print('Error, {} is not a directory.'.format(dir))

processDirectory(os.path.abspath(sys.argv[1]))
print(str(lengthMap))
