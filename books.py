import matplotlib.pyplot as plt; plt.rcdefaults()
from collections import defaultdict
import sys
import string
import os
import numpy as np

stopwords = set()

punctuation = set(string.punctuation)
dir = "booksdir"

def parsefile(filename):
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print(filename, "is missing from your current directory")
        sys.exit(-1) # quits the program
    lines = file.readlines()
    file.close()
    return lines

def createMap(lines):
    words = defaultdict(int)
    for l in lines:
        l = l.strip()
        l = ''.join(ch for ch in l if ch not in punctuation)
        l = l.lower().split(" ")
        for w in l:
            words[w] += 1
    return words

if __name__ == "__main__":
    inputword = "the"

    directory = os.fsencode(dir)

    books = {}
    for file in os.listdir(directory):
         filename = os.fsdecode(file)
         if filename.endswith(".txt"):
             try:
                 file_name = dir+'/'+filename
             except FileNotFoundError:
                 print("Cannot find file")
                 sys.exit(-1)

             lines = parsefile(file_name)
             words = createMap(lines)
             books[filename] = words

    objects = tuple(books.keys())

    y_pos = np.arange(len(objects))

    performance = []
    for title in objects:
        performance.append(books[title][inputword])

    #switch to plotly
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('frequency')
    plt.title('input word frequency in books')

    plt.show()
