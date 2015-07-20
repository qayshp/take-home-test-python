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

def process_file(file, openZip=None):
    if file.lower().endswith(".txt"):
        logging.info('Found txt file: {}'.format(file))
        if (openZip):
            process_txt(openZip.open(file, 'r'))
        else:
            process_txt(open(file))
    elif file.lower().endswith(".zip"):
        logging.info('Found zip file: {}'.format(file))
        process_zip(file)
        logging.info('Done with zip file: {}'.format(file))

def process_zip(file):
    with zipfile.ZipFile(file, 'r') as openZip:
        for zippedFile in openZip.namelist():
            process_file(zippedFile, openZip)

def process_txt(file):
    for line in file:
        for word in line.split():
            logging.debug("%s :%s", len(word), word)
            lengthMap[len(word)] += 1

def process_directory(dir):
    if (os.path.isdir(dir)):
        for root, dirs, files in os.walk(dir):
            for file in files:
                process_file(os.path.join(root, file))
    else:
        print('Error, {} is not a directory.'.format(dir))

log_level = sys.argv[2] if len(sys.argv)>2 else getattr(logging, "INFO")
logging.basicConfig(level=log_level)

process_directory(os.path.abspath(sys.argv[1]))
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
