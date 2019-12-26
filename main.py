#~~~~~ REQUIRED LIBRARIES ~~~~~#

#1 ~ for cross-platform file location
import os

#2 ~ natural language processing toolkit - NLTK
import nltk 
#download relevant NLTK data, this needs to be done just once for first time users
#alternatively you can also use the command line to download whatever NLTK data package you need see https://www.nltk.org/data.html
#nltk.download('all')


#~~~~~ MAIN CODE ~~~~~#

#variable declarations
word_count_list = []
word_counter = 0
counter = 0
total_word_count = 0
total_word_frequency = 0
apple_words = []

#set text file location, mine is in downloads
downloads = os.path.join(os.path.expanduser("~"), "Downloads")
filePath = os.path.join(downloads, "Apple_Event_2019_09.txt")

#open the required text file
apple_file = open(filePath, encoding='utf-8-sig')

#loop through file and append all the words to the first list
for x in apple_file.read().split():
    apple_words.append(x)
    total_word_count += 1

#generate and remove stop words from our apple words
stop_words_list = list(nltk.corpus.stopwords.words("english"))

i = 0
j = i + 1

while i < len(stop_words_list):
    while j < len(apple_words):
        if apple_words[j] == stop_words_list[i]:
            del apple_words[j]
            total_word_count = total_word_count - 1
        else:
            j = j + 1
    
    i = i + 1
    j = i + 1
            

#make a copy of the list so we can count word frequencies once we clean the original list of dupes
copy_apple_words = apple_words.copy()

#set initial while loop values
i = 0
j = i + 1

#start with first word and loop through whole list to check if it appears and delete
#update total_word_count as words get deleted
while i < total_word_count:
    while j < total_word_count:
        if apple_words[i] == apple_words[j]:
            del apple_words[j]
            total_word_count = total_word_count - 1
        else:
            j = j + 1
    i = i + 1
    j = i + 1


#loop over the copy list by comparing words from the unique list and counting word frequency
for i in range(0, len(apple_words)):
    for k in range(0, len(copy_apple_words)):
        if apple_words[i] == copy_apple_words[k]:
            word_counter += 1
    word_count_list.append(word_counter)
    word_counter = 0

#sum the counts to see if the total word count is the same as original list length
for n in range(0, len(word_count_list)):
    total_word_frequency = total_word_frequency + word_count_list[n]

#test if found total word frequency is the same as the length of original word list 
assert total_word_frequency == len(copy_apple_words), "FALSE - sum of found word frequencies is not equal to original list length"

#sort word frequencies in descending order
for word_count in range(0, len(word_count_list)):
    for other_word_count in range(word_count + 1, len(word_count_list)):
        if word_count_list[word_count] < word_count_list[other_word_count]:
            
            #swap elements in frequency list
            tmp = word_count_list[word_count]
            word_count_list[word_count] = word_count_list[other_word_count]
            word_count_list[other_word_count] = tmp

            #swap elements in unique word list to correspond to word_count_list
            tmp2 = apple_words[word_count]
            apple_words[word_count] = apple_words[other_word_count]
            apple_words[other_word_count] = tmp2


#print 10 top used words in descending order
print (word_count_list[:11])
print(apple_words[:11])            

#close the file when finished
apple_file.close()

