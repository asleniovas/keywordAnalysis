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