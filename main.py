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

#3 ~ for generating word clouds
from wordcloud import WordCloud

#4 ~ for image processing with WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#5 ~ our classes from other files that hold various text cleaning and manipulation methods
from textCleaner import TextCleaner
from textCounter import TextCounter

# |_             _|
# |   MAIN CODE   |
# |               |

#variable declarations
word_counter = 0
file_strings = []
string_dictionary = {}

#generate stop words array with help of NLTK
stop_words_list = list(nltk.corpus.stopwords.words("english"))

#add custom stop words. Youtube specific transcripts have [Applause] and [Music] for example
#as well as apple context words and others found during first processings
new_stop_words = ["[applause]", "[music]", "apple", "ipad", 
                  "iphone", "we're", "that's", "11", "thank",
                  "like", "we've", "let's", "pro"]

stop_words_list = stop_words_list + new_stop_words


# |_                                           _|
# |   STEP 1 - TEXT FILE LOCATION AND OPENING   |
# |                                             |

#set text file location and open, mine is in Documents
repo = os.path.join(os.path.expanduser("~"), "Documents/repos/keywordAnalysis")
file_path = os.path.join(repo, "Apple_Event_2019_09.txt")

file_open = open(file_path, encoding="utf-8-sig")


# |_                                            _|
# |   STEP 2 - TEXT CLEANING AND NORMALISATION   |
# |                                              |

#convert to lowercase and split text into words
file_strings = file_open.read().lower().split()

#close the file after producing required array
file_open.close()

#clean words from stop words by calling compareRemove() function
cleaner_class = TextCleaner()
updated_file_strings = cleaner_class.compareRemove(stop_words_list, file_strings)


#make a copy of the list so we can count word frequencies once we clean the original list of dupes and other clutter
copy_file_strings = updated_file_strings.copy()
unique_file_strings = cleaner_class.removeDuplicates(updated_file_strings)

#producing a dictionary with word occurrences 
counter_class = TextCounter()
string_dictionary = counter_class.countElements(copy_file_strings)

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