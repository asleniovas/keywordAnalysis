class TextCleaner:

    def __init__(self):
        pass

    #function accepts 2 arrays. Compares elements from 1st array to 2nd to see if they exist in 2nd, 
    #and removes them from 2nd array. 
    def compareRemove(self, array1 = [], array2 = []):

        #starting iteration values
        i = 0
        j = 0

        #determining array lengths
        array1_length = len(array1)
        array2_length = len(array2)

        while i < array1_length:
            while j < array2_length:

                #compare element from first array to second array, remove element if same, and update second array length
                if array1[i] == array2[j]:

                    del array2[j]
                    array2_length = len(array2)

                #otherwise move j forward
                else:
                    j = j + 1

            #when 2nd while loop is done move i forward and reset j to 0
            i = i + 1
            j = 0

        return array2


    #function removes duplicates from single array
    def removeDuplicates(self, array1 = []):

        #starting iteration values
        i = 0
        j = i + 1

        #determining array length
        array1_length = len(array1)

        #loop through given array by comparing i element if it occurs further in array and remove
        while i < array1_length:
            while j < array1_length:

                #if true remove and update array length
                if array1[i] == array1[j]:
                    del array1[j]
                    array1_length = len(array1)
                
                #otherwise move forward in array with j
                else:
                    j = j + 1
            
            i = i + 1
            j = i + 1

        return array1

    #function turns 1 array with keys and 2nd array with values into dictionary 
    def arraysToDict(self, keysArray = [], valuesArray = []):

        #initilize empty dictionary
        dictionary1 = {}

        #loop through all keys by adding them and their values to the dict
        for i in keysArray:
            dictionary1[keysArray[i]] = valuesArray[i]

        return dictionary1  
