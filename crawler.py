import zipfile
import gzip
import numpy as np
import magic
import sys
import os
import tarfile
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

    elif file.lower().endswith(".tgz") or file.lower().endswith(".tar.gz"):
        logging.info('Found tgz file: {}'.format(file))
        # process_tgz(file)
        logging.info('Done with tgz file: {}'.format(file))

def process_zip(file):
    with zipfile.ZipFile(file=file, mode='r') as openZip:
        for zippedFile in openZip.namelist():
            process_file(zippedFile, openZip)

def process_tgz(file):
    with tarfile.open(name=file, mode='r:gz') as openZip:
        for zippedFile in openZip.getnames():
            process_file(zippedFile, openZip)

def process_txt(file):
    for line in file:
        for word in line.split():
            logging.debug("%s :%s", len(word), word)
            lengthMap[len(word)] += 1

def process_directory(dir):
    if (os.path.isdir(dir)):
        for root, dirs, files in os.walk(top=dir, followlinks=False):
            for file in files:
                process_file(os.path.join(root, file))
    else:
        print('Error, {} is not a directory.'.format(dir))

def create_plot_array(data):
    x = []
    for key in data:
        for i in range(data[key]):
            x.append(key)
    return x

def draw_histogram(data):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    numBins = 50
    ax.hist(create_plot_array(data),numBins,color='green',alpha=0.8)
    plt.show()

log_level = sys.argv[2] if len(sys.argv)>2 else getattr(logging, "INFO")
logging.basicConfig(level=log_level)

process_directory(os.path.abspath(sys.argv[1]))
logging.info(str(lengthMap))
draw_histogram(lengthMap)
