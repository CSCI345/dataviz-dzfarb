from collections import defaultdict
import sys
import string
import os
import numpy as np
import plotly.graph_objects as go
from ipywidgets import interact_manual
#import nbinteract as nbi

punctuation = set(string.punctuation)
dir = "booksdir"

def parsefile(filename):
    file = open(filename, "r")
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

    book_titles = books.keys()

    y_pos = np.arange(len(book_titles))

    def update(word):
        inputword = word
        performance = []
        for title in book_titles:
            performance.append(books[title][inputword])
        fig = go.Figure([go.Bar(x=book_titles, y=performance, name=inputword)])
        fig.show()
        return

    interact_manual(update, word="type word here");
