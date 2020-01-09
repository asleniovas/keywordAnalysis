# |_                      _|
# |   REQUIRED LIBRARIES   |
# |                        |

#1 ~ for cross-platform file location
import os

#2 ~ natural language processing toolkit - NLTK
import nltk 
#download relevant NLTK data, this needs to be done just once for first time users
#alternatively you can also use the command line to download whatever NLTK data package you need 
#see https://www.nltk.org/data.html

#nltk.download('all')

#3 ~ for generating word clouds
from wordcloud import WordCloud

#4 ~ for image processing with WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#5 ~ our class from other file that holds various text cleaning methods
from textCleaner import TextCleaner

# |_             _|
# |   MAIN CODE   |
# |               |

#variable and object declarations
word_counter = 0
counter = 0
file_strings = []
string_dictionary = {}

#generate stop words array with help of NLTK
stop_words_list = list(nltk.corpus.stopwords.words("english"))

#add custom stop words. Youtube specific transcripts have [Applause] and [Music] for example
#as well as apple context words and others found during first processings
new_stop_words = ["[applause]", "[music]", "apple", "ipad", 
                  "iphone", "we're", "that's", 
                  "we've", "let's", "pro"]

stop_words_list = stop_words_list + new_stop_words


# |_                                           _|
# |   STEP 1 - TEXT FILE LOCATION AND OPENING   |
# |                                             |

#set text file location and open, mine is in Documents
repo = os.path.join(os.path.expanduser("~"), "Documents/repos/keywordAnalysis")
file_path = os.path.join(repo, "Apple_Event_2019_09.txt")
#open file, convert to lowercase and split each word creating a list
file_open = open(file_path, encoding='utf-8-sig')
file_strings = file_open.read().lower().split()
#close the opened file
file_open.close()

# |_                                            _|
# |   STEP 2 - TEXT CLEANING AND NORMALISATION   |
# |                                              |


#clean apple words from stop words by calling compareRemove() function
cleaner_class = TextCleaner()
updated_file_strings = cleaner_class.compareRemove(stop_words_list, file_strings)


#make a copy of the list so we can count word frequencies once we clean the original list of dupes and other clutter
copy_file_strings = updated_file_strings.copy()
unique_file_strings = cleaner_class.removeDuplicates(updated_file_strings)


#loop over the copy list by comparing words from the unique list and counting word frequency
for i in range(0, len(unique_file_strings)):
    for k in range(0, len(copy_file_strings)):

        if unique_file_strings[i] == copy_file_strings[k]:
            word_counter += 1

    #append word and frequency to dictionary item
    string_dictionary[unique_file_strings[i]] = word_counter

    #word_count_list.append(word_counter)
    word_counter = 0

#sort word frequencies in descending order
'''
for word_count in range(0, len(word_count_list)):
    for other_word_count in range(word_count + 1, len(word_count_list)):

        if word_count_list[word_count] < word_count_list[other_word_count]:
            
            #swap elements in frequency list
            tmp = word_count_list[word_count]
            word_count_list[word_count] = word_count_list[other_word_count]
            word_count_list[other_word_count] = tmp

            #swap elements in unique word list to correspond to word_count_list
            tmp2 = unique_apple_words[word_count]
            unique_apple_words[word_count] = unique_apple_words[other_word_count]
            unique_apple_words[other_word_count] = tmp2
'''

#print 10 top used words in descending order
#print(word_count_list[:21])
#print(unique_apple_words[:21])            

#convert word_count_list and unique_apple_words to a dictionary for word cloud generation
#apple_dictionary = cleaner_class.arraysToDict(unique_apple_words, word_count_list)

#close the file when finished
#apple_file.close()


# |_                                       _|
# |    STEP X - WORD CLOUD VISUALISATION    |
# |                                         |

apple_logo = os.path.join(repo, "apple.png")
apple_mask = np.array(Image.open(apple_logo))

#generating the word cloud
wc = WordCloud(background_color="white", max_words=50, mask=apple_mask)
wc.generate_from_frequencies(string_dictionary)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()