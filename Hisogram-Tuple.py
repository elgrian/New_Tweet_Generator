import sys
from dictionary_words import list_convert, read_text_file

def histogram(source_text):
    '''Turns a list of text into a list of tuples'''
    list_of_tuples = []
    list_of_tuples.append((source_text[0], 1))
    
    for word in source_text:
        word_found = False
        for index, item in enumerate(list_of_tuples):
            if item[0] == word: #If the item is the the word from source_text
                word_found = True
                placeholder_count = item[1] + 1
                tuple_placeholder = (word, placeholder_count)
                item, tuple_placeholder, item
                list_of_tuples[index] = item
        if word_found == False:
            list_of_tuples.append((word, 1))
            
    return list_of_tuples
    
    
    
def frequency(word, histogram):
    '''Takes a word and returns the number of times it occurs'''
    word_count = 0
    for item in histogram:
        if item[0] == word:
            count = item[1]
    return word_count
    
    
def word_types(histogram):
    '''Takes a histogram and returns number of word types in the histogram'''
    word_count = 0
    for item in histogram:
        word_count += 1
    return word_count
    
    
    
def main():
    text_file = read_text_file('harry_potter.txt')
    text_list = list_convert(text_file)
    list_of_tuples = histogram(text_list)
    print(list_of_tuples)
    
    unique_word = unique_words(list_of_tuples)
    print(unique_words)


if __name__ == '__main__':
    main()
        