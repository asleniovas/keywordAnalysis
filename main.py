#---------------------------- REQUIRED LIBRARIES ------------------------------

import os
from PIL import Image
from string import punctuation

import nltk 
import pandas
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from modules.textCleaner import TextCleaner
from modules.textCounter import TextCounter

#-------------------------- MAIN CLEANING FUNCTION ----------------------------

def cleanTextFiles (data_folder, text_files = [], stop_words = {}):

    dictionary_list = []

    #loop through each text file, read and clean
    for i in range(0, len(text_files)):

        file_path = os.path.join(data_folder, text_files[i])
        file_open = open(file_path, encoding="utf-8-sig").read()

        #remove punctuation leave apostrophes, convert to lowercase and split
        my_punctuation = punctuation.replace("'", "")
        text = file_open.translate(str.maketrans("", "", my_punctuation))
        file_strings = text.lower().split()

        #clean file_strings from stop words
        cleaner = TextCleaner()
        updated_file_strings = cleaner.compareRemove(stop_words, file_strings)

        #lemmatize updated_file_strings
        lemmtzr = nltk.stem.wordnet.WordNetLemmatizer()
        lemmas = [lemmtzr.lemmatize(token) for token in updated_file_strings]

        #produce a dictionary with word occurrence counts
        counter = TextCounter()
        string_dictionary = counter.countElements(lemmas)

        dictionary_list.append(string_dictionary)

    return dictionary_list

#--------------------------------- MAIN CODE ----------------------------------

if __name__ == "__main__":

    #text file names
    text_files = ["Apple_Event_2017_09.txt", "Apple_Event_2018_09.txt" 
                  ,"Apple_Event_2019_09.txt"]

    #generate standard stop words set with NLTK and add custom ones
    stop_words = set(nltk.corpus.stopwords.words("english"))
    new_stop_words = {"us", "gonna", "series", "take", "10", "11", "8", "i"
                      , "4", "applause", "apple", "ipad", "there's", "we'd" 
                      , "thank", "like", "we've", "look", "one", "what's"
                      , "i'm", "xs", "get", "i'd", "i'll", "let's", "pro"
                      , "iphone", "we're", "that's", "they're", "can't"}
    
    stop_words = stop_words.union(new_stop_words)

    #set text file location
    data_folder = os.path.join(os.path.expanduser("~")
                               , "Documents/repos/keywordAnalysis/data")
    
    #call main cleaning function
    clean_dict_list = cleanTextFiles(data_folder, text_files, stop_words)

    
    #initialize wordcloud visualisation and set params
    img_folder = os.path.join(os.path.expanduser("~")
                              , "Documents/repos/keywordAnalysis/img")
    
    png_image = os.path.join(img_folder, "apple.png")
    png_mask = np.array(Image.open(png_image))
    wc = WordCloud(background_color="black", max_words=150
                   , mask=png_mask, colormap="cool")

    
    #start plotting figure based on quantity of processed files
    list_length = len(clean_dict_list)
    fig, axs = plt.subplots(1, list_length, figsize=(6,3))
    fig.suptitle("Apple September Event Most Frequently Used Words", y="0.80"
                 , color="#f5f5f7", horizontalalignment="center"
                 , fontsize="13", verticalalignment="center")
    
    fig.set_facecolor('black')

    #loop through the list returned by cleanTextFiles() and adjust subplots
    for e in range(0, list_length):

        wc.generate_from_frequencies(clean_dict_list[e])
        axs[e].imshow(wc, interpolation="bilinear")

        #x-axis params
        axs[e].set_xlabel(text_files[e][12:16], fontfamily="sans-serif"  
                          , fontsize="13", color="#f5f5f7")
        axs[e].set_xticklabels([])
        axs[e].set_xticks([])
        axs[e].xaxis.set_label_coords(0.5, 0.20)

        #y-axis params
        axs[e].set_yticklabels([])
        axs[e].set_yticks([])

    #adjust spacing between subplots
    plt.subplots_adjust(wspace= -0.3, right=1, left=0)
    

    fig.savefig("wordcloud.png", facecolor=fig.get_facecolor() 
                , edgecolor="black", dpi=200)
    plt.show()