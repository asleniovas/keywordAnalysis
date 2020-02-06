#---------------------------- REQUIRED LIBRARIES -----------------------------

import os
from PIL import Image
import string

import nltk 
import pandas
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from modules.textCleaner import TextCleaner
from modules.textCounter import TextCounter

#-------------------------- MAIN CLEANING FUNCTION ---------------------------

def cleanTextFiles (repo, text_files = [], stop_words = {}):

    dictionary_array = []

    #loop through each text file, open and clean
    for i in range(0, len(text_files)):

        file_path = os.path.join(repo, text_files[i])
        file_open = open(file_path, encoding="utf-8-sig").read()

        #remove punctuation, convert to lowercase, and split words
        text = file_open.translate(str.maketrans("", "", string.punctuation.replace("'","")))
        file_strings = text.lower().split()

        #clean file_strings from stop words by calling compareRemove() function
        cleaner_class = TextCleaner()
        updated_file_strings = cleaner_class.compareRemove(stop_words, file_strings)

        #lemmatize updated_file_strings
        lem_class = nltk.stem.wordnet.WordNetLemmatizer()
        lemmas = [lem_class.lemmatize(token) for token in updated_file_strings]

        #producing a dictionary with word occurrence counts
        counter_class = TextCounter()
        string_dictionary = counter_class.countElements(lemmas)

        dictionary_array.append(string_dictionary)

    return dictionary_array

#--------------------------------- MAIN CODE ---------------------------------

if __name__ == "__main__":

    text_files = ["Apple_Event_2017_09.txt", "Apple_Event_2018_09.txt", 
                  "Apple_Event_2019_09.txt"]

    #generate stop words set with help of NLTK and add custom ones
    stop_words = set(nltk.corpus.stopwords.words("english"))
    new_stop_words = {"applause", "music", "apple", "ipad", "us", "gonna", "series", 
                      "thank", "like", "we've", "pro", "i'm", "xs", "get", "4",
                      "iphone", "we're", "that's", "11", "10", "8", "look"}
    
    stop_words = stop_words.union(new_stop_words)

    #set text file location, and call the main function
    repo = os.path.join(os.path.expanduser("~"), "Documents/repos/keywordAnalysis/data")
    dictionary_array = cleanTextFiles(repo, text_files, stop_words)


    #initialize word cloud visualisation
    png_location = os.path.join(os.path.expanduser("~"), "Documents/repos/keywordAnalysis/img")
    png_image = os.path.join(png_location, "apple.png")
    png_mask = np.array(Image.open(png_image))

    wc = WordCloud(background_color="black", max_words=40, 
                   mask=png_mask, colormap="plasma")

    #subplot quantity based on the number of text files processed
    fig, axs = plt.subplots(1, len(dictionary_array))
    fig.suptitle("Apple September Event Most Frequently Used Words",
                 color="#f5f5f7", horizontalalignment="center", x=0.5, y=0.75)

    #loop through the array returned by cleanTextFiles() and plot
    for e in range(0, len(dictionary_array)):

        wc.generate_from_frequencies(dictionary_array[e])
    
        axs[e].imshow(wc, interpolation="bilinear")

        #x-axis tick params
        axs[e].set_xlabel(text_files[e][12:16], color="#f5f5f7", fontfamily="sans-serif")
        axs[e].set_xticklabels([])
        axs[e].set_xticks([])
        axs[e].xaxis.set_label_coords(0.5, 0.20)

        #y-axis tick params
        axs[e].set_yticklabels([])
        axs[e].set_yticks([])

    plt.subplots_adjust(wspace=-0.3)
    plt.show()