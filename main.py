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

#4 ~ for generating word clouds
from wordcloud import WordCloud

#5 ~ for image processing with WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#6 ~ our classes from other files that hold various text cleaning and manipulation methods
from textCleaner import TextCleaner
from textCounter import TextCounter

# |_             _|
# |   MAIN CODE   |
# |               |


#generate stop words array with help of NLTK
stop_words_list = list(nltk.corpus.stopwords.words("english"))

#add custom stop words. Youtube specific transcripts have [Applause] and [Music] for example
#as well as Apple context words and others found during first processings
new_stop_words = ["[applause]", "[music]", "apple", "ipad", 
                  "iphone", "we're", "that's", "11", "thank",
                  "like", "we've", "let's", "pro"]

stop_words_list = stop_words_list + new_stop_words



# |_                                           _|
# |   STEP 1 - TEXT FILE LOCATION AND OPENING   |
# |                                             |


text_files = ["Apple_Event_2017_09.txt", "Apple_Event_2018_09.txt", "Apple_Event_2019_09.txt"]

for single_file in range(1, len(text_files)):

    #set text file location and open, mine is in Documents
    repo = os.path.join(os.path.expanduser("~"), "Documents/repos/keywordAnalysis")
    file_path = os.path.join(repo, text_files[single_file])

    file_open = open(file_path, encoding="utf-8-sig").read()

# |_                                            _|
# |   STEP 2 - TEXT CLEANING AND NORMALISATION   |
# |                                              |

    #remove punctiation, convert to lowercase, and split words
    text = file_open.translate(str.maketrans("", "", string.punctuation))
    file_strings = text.lower().split()

    #close the file after producing required array
    file_open.close()

    #clean words from stop words by calling compareRemove() function
    cleaner_class = TextCleaner()
    updated_file_strings = cleaner_class.compareRemove(stop_words_list, file_strings)

    #producing a dictionary with word occurrence counts
    counter_class = TextCounter()
    string_dictionary = counter_class.countElements(updated_file_strings)

# |_                                       _|
# |    STEP X - WORD CLOUD VISUALISATION    |
# |                                         |

png_image = os.path.join(repo, "apple.png")
png_mask = np.array(Image.open(png_image))

#generating the word cloud
wc = WordCloud(background_color="black", max_words=50, 
               mask=png_mask, colormap="plasma")
wc.generate_from_frequencies(string_dictionary)

fig, (ax1, ax2) = plt.subplots(1, 2)

plt.subplots_adjust(wspace=-0.3)

ax1.imshow(wc, interpolation="bilinear")
ax2.imshow(wc, interpolation="bilinear")
ax1.axis("off")
ax2.axis("off")
plt.show()