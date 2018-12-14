'''
    Takes in a word file, returns a historgram of everything, the amount of unique words
    in the text file and the value of each wordself.

USAGE: python3 ./word_frequency.py'''

import sys, string
from dictionary_sentence import read_text_file, list_convert

def histogram(source_text):
    '''Takes in a list of text and returns histogram as a dictionary'''
    histogram_dict = {}
    for word in source_text:
        if histogram_dict.get(word) is None:
            histogram_dict[word] = 1
        else:
            histogram_dict[word] += 1
    return histogram_dict
    
def word_types(histogram_dict): #'''Use word_types'''
    #'''Takes histogram and returns number of word tokens'''
    count = 0 
    for key in histogram_dict:
        count += 1
    return count
    
def frequency(word, histogram):
    
    '''Takes in a word, histogram, and returns the words value'''
    count = 0
    for key in histogram: 
        if word == key:
            count = histogram[key]
    return count
    
def main():
    file_text = read_text_file('harry_potter.txt')
    text_list = list_convert(file_text)
    text_list[:] = [i.translate(str.maketrans('','',string.punctuation)) for i in text_list]
    my_histogram = histogram(text_list)
    print(my_histogram)
    
    number_of_word_types = unique_wirds(my_histogram)
    print("The Number of unique words is: {}".format(word, word_count))
    
    if __name__ == '__main__':
        main()