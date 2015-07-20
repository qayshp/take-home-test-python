import zipfile
import gzip
import numpy as np
import magic
import sys
import os
import logging
import getopt
import matplotlib.pyplot as plt
from collections import defaultdict

lengthMap = defaultdict(int)

def processFile(file, openZip=None):
    if file.lower().endswith(".txt"):
        logging.info('Found txt file: {}'.format(file))
        if (openZip):
            processTxt(openZip.open(file, 'r'))
        else:
            processTxt(open(file))
    elif file.lower().endswith(".zip"):
        logging.info('Found zip file: {}'.format(file))
        processZip(file)
        logging.info('Done with zip file: {}'.format(file))

def processZip(file):
    with zipfile.ZipFile(file, 'r') as openZip:
        for zippedFile in openZip.namelist():
            processFile(zippedFile, openZip)

def processTxt(file):
    for line in file:
        for word in line.split():
            logging.debug("%s :%s", len(word), word)
            lengthMap[len(word)] += 1

def processDirectory(dir):
    if (os.path.isdir(dir)):
        for root, dirs, files in os.walk(dir):
            for file in files:
                processFile(os.path.join(root, file))
    else:
        print('Error, {} is not a directory.'.format(dir))

log_level = sys.argv[2] if len(sys.argv)>2 else getattr(logging, "INFO")
logging.basicConfig(level=log_level)

processDirectory(os.path.abspath(sys.argv[1]))
print(str(lengthMap))


fig = plt.figure()
ax = fig.add_subplot(111)

x = []
for key in lengthMap:
    for i in range(lengthMap[key]):
        x.append(key)
numBins = 50
ax.hist(x,numBins,color='green',alpha=0.8)
plt.show()
