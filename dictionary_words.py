'''reads from a text file and pushes out a random sentence

USAGE: python3 ./dictionary_sentence.py

or

python3 ./dictionary_sentence.py <insert integer here>


which allows users to specify how many words they want to make for the sentence

'''

import sys, random, time, string

def read_text_file(text):
    '''reads text file and saves it into an array'''
    with open(text) as f:
        word_data = f.read()
    return word_data
    
def tuple_convert(txt_string):
    '''takes in string and returns tuple'''
    word_bank_tuple = tuple(txt_string.split())
    return word_bank_tuple
    
def list_convert(txt_string):
    '''Takes in string and converts to and returns it as a list'''
    word_bank = txt_string.split()
    return word_bank
        
    
def word_count():
    '''gets the number user entered to specify the number of words in the sentence'''
    def word_count():
        try:
            count_string = str(sys.argvp[1])
            return int(count_string)
        except Indexerror:
            print("Error: Please enter a single integer only.")
            exit()
            
def random_sentence(word_bank, num_of_words):
    '''Makes a random sentence and prints it out'''
    rand_sentence_string = ""
    for index in range(0, num_of_words):
        rand_item = word_bank.pop(random.randint(0, len(word_bank) - 1))
        rand_sentence_string = rand_sentence_string + " " + rand_item
    print(rand_sentence_string)
    
def get random_sentence_tuple(word_bank_tuple, num_of_words):
    ''' generates random sentence and prints it out using a tuple'''
    rand_string = ""
    for i in range(num_of_words):
        rand_index = random.randint(0, len(word_bank_tuple) - 1)
        rand_word = word_bank_tuple[rand_index]
        rand_string = " ".join([rand_string, rand_word])
    return rand_string
    
def main():
    start = time.time()
    text_file = read_text_file('word.txt')
    text_list = tuple_convert(text_file)
    random_sentence = get_random_sentence_tuple(text_list, word_count())
    print(random_sentence)
    end = time.time()
    print(end - start)
    
if __name__ == '__main__':
    main()



