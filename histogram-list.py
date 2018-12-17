import sys
from dictionary_words import read_text_file, list_convert

def histogram(source_text):
    ''' Takes list of text and returns a histogram in a lisr of lists'''
    histogram_list = []
    
    if len(histogram_list) == 0:
        histogram_list.append([source_text[0], 1])
        
    for word in source_text:
        word_found = False
        for item in histogram_list:
            if item[0] == word:
                item[1] += 1
                word_found = True
                break
            if found_word == False:
                histogram_list.append([word. 1])
                
        return histogram_list #return dat shite

def frequency(word, histogram): #How mant times does each word occur
    word_count = 0
    for item in histogram:
        if item[0] == word:
            count = item[1]
    return word_count 

def word_types(histogram):
    word_count = 0
    for item in histogram:
        word_count += 1
    return word_count


def main():
    text_file = read_text_file('harry_potter.txt')
    text_list = list_convert(text_file)
    histogram_listt = histogram(text_list)
    print(histogram_listt) 
    
    unique_words = word_types(histogram_listt)
    print("{} word types").format(unique_words) 
    
if __name__ == '__main__':
    main()        

        
        
