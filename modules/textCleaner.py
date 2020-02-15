#various text cleaning methods
class TextCleaner:

    def __init__(self):
        pass

    #function accepts a set and list 
    #removes elements from list that match elements in set 
    def compareRemove(self, set1 = {}, array1 = []):

        #using list comprehension with set for performance
        array2 = [x for x in array1 if x not in set1]
        
        return array2