#Dizzy Farbanish
#CS345
#HW 1

#This is a program that reads in book text files from a directory and
#creates a bar graph with an interactive textbox, that allows you to
#search and compare words and phrase counts between books

#imports
from collections import defaultdict
import sys
import string
import os
import numpy as np
import plotly.graph_objects as go
from ipywidgets import interact_manual

#initialize global variables
punctuation = set(string.punctuation)
#file name of book directory
DIRECTORY = "booksdir"
#parameter for maximum length of a phrase to be inserted into dictionary
PHRASE_LENGTH = 6

#parses the files
def parsefile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    return lines

#generates dictionary of words and phrases to counts
def createMap(lines):
    words = defaultdict(int)
    for l in lines:
        l = l.strip()
        l = ''.join(ch for ch in l if ch not in punctuation)
        l = l.lower().split(" ")
        for i in range(len(l)):
            baseword = l[i]
            words[baseword] += 1
            for j in range(1, PHRASE_LENGTH):
                if (i + j) >= len(l):
                    break
                baseword = baseword + ' ' + l[j]
                words[baseword] += 1
    return words

#main function
if __name__ == "__main__":

    dir = os.fsencode(DIRECTORY)

    #iterates through all books in the directory
    #builds dictionary of all books and word and phrase counts for each book
    books = {}
    for file in os.listdir(dir):
         filename = os.fsdecode(file)
         if filename.endswith(".txt"):
             try:
                 file_name = DIRECTORY+'/'+filename
             except FileNotFoundError:
                 print("Cannot find file")
                 sys.exit(-1)
             lines = parsefile(file_name)
             words = createMap(lines)
             books[filename] = words

    book_titles = list(books.keys())

    y_pos = np.arange(len(book_titles))

    #function that handles text box input
    def update(phrase):
        inputword = phrase
        performance = []
        for title in book_titles:
            performance.append(books[title][inputword])
        fig = go.Figure([go.Bar(x=book_titles, y=performance, name=inputword)])
        fig.show()
        return

    #enables interactive text box
    interact_manual(update, phrase="type word here");
