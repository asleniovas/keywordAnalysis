from collections import Counter

class TextCounter:

    def __init__(self):
        pass

    #function counts element occurences in array and returns a dictionary with counts
    def countElements(self, strings = []):

        counts_dict = Counter(strings)

        return counts_dict