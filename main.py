# |_                      _|
# |   REQUIRED LIBRARIES   |
# |                        |

#1 ~ for cross-platform file location
import os

#2 ~ natural language processing toolkit - NLTK
import nltk 
#download relevant NLTK data, this needs to be done once for first time users 
#see https://www.nltk.org/data.html

#nltk.download('all')

#3 for quick string manipulations
import string
import pandas

#4 ~ for generating word clouds
from wordcloud import WordCloud

#5 ~ for image processing with WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#6 ~ our classes from other files that hold various text cleaning and manipulation methods
from textCleaner import TextCleaner
from textCounter import TextCounter

#main function, returns an array of dictionaries
def cleanTextFiles (repo, text_files = [], stop_words_list = []):

    dictionary_array = []

    #loop through each text file, open and clean
    for i in range(0, len(text_files)):

        file_path = os.path.join(repo, text_files[i])

        file_open = open(file_path, encoding="utf-8-sig").read()

        #remove punctuation, convert to lowercase, and split words
        text = file_open.translate(str.maketrans("", "", string.punctuation.replace("'","")))
        file_strings = text.lower().split()

        #clean words from stop words by calling compareRemove() function
        #cleaner_class = TextCleaner()
        #updated_file_strings = cleaner_class.compareRemove(stop_words_list, file_strings)

        #explore additional potential stopwords -> 
        #by printing most frequently used words after initial cleaning
        #print(pandas.Series(updated_file_strings).value_counts()[:20])

        #producing a dictionary with word occurrence counts
        counter_class = TextCounter()
        string_dictionary = counter_class.countElements(file_strings)

        #add final dictionary to array
        dictionary_array.append(string_dictionary)

    return dictionary_array

#main code
if __name__ == "__main__":

    text_files = ["Apple_Event_2017_09.txt", "Apple_Event_2018_09.txt", 
                  "Apple_Event_2019_09.txt"]

    #generate stop words set with help of NLTK
    stop_words_list = list(nltk.corpus.stopwords.words("english"))

    #add custom stop words. Order is not important so->
    #to avoid duplicates we convert to set and back to list
    new_stop_words = ["applause", "music", "apple", "ipad", "us", "gonna", "series", 
                  "thank", "like", "we've", "pro", "i'm", "xs", "get",
                  "iphone", "we're", "thats", "11", "10", "8", "look", "4"]

    stop_words_list = list(set(stop_words_list + new_stop_words))

    #set text file location, mine is in Documents
    repo = os.path.join(os.path.expanduser("~"), "Documents/repos/keywordAnalysis")

    #call cleanText function
    dictionary_array = cleanTextFiles(repo, text_files, stop_words_list)

    #start visualisation with image processing
    png_image = os.path.join(repo, "apple.png")
    png_mask = np.array(Image.open(png_image))

    #instantiate the wordcloud with desired params
    wc = WordCloud(background_color="black", max_words=40, 
                   mask=png_mask, colormap="plasma", stopwords=stop_words_list)

    fig, axs = plt.subplots(1, len(dictionary_array))
    fig.suptitle("Apple September Event Most Frequently Used Words",
                 color="#f5f5f7", horizontalalignment="center", x=0.5, y=0.75)

    #loop through all dictionaries containing word counts and plot
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