import matplotlib
from collections import defaultdict
import sys
import string
import os
import numpy as np

stopwords = set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
                         "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself",
                         "she", "her", "hers", "herself", "it", "its", "itself", "they", "them",
                         "their", "theirs", "themselves", "what", "which", "who", "whom", "this",
                         "that", "these", "those", "am", "is", "are", "was", "were", "be", "been",
                         "being", "have", "has", "had", "having", "do", "does", "did", "doing",
                         "a", "an", "the", "and", "but", "if", "or", "because", "as", "until",
                         "while", "of", "at", "by", "for", "with", "about", "against", "between",
                         "into", "through", "during", "before", "after", "above", "below", "to",
                         "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
                         "further", "then", "once", "here", "there", "when", "where", "why",
                         "how", "all", "any", "both", "each", "few", "more", "most", "other",
                         "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                         "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", ""])

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

def removeStops(words):
    clean_words = []
    for w in words:
        if w in self.stopword_set:
            continue
        clean_words.append(w)
    return clean_words

def createMap(lines):
    words = defaultdict(int)
    for l in lines:
        l = l.strip()
        l = ''.join(ch for ch in l if ch not in punctuation)
        l = l.lower().split(" ")
        for w in l:
            if w not in stopwords:
                words[w] += 1
    return words

if __name__ == "__main__":
    testword = "while"

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
        

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('Programming language usage')

    plt.show()
