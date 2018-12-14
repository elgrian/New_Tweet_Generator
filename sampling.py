import sys, random
from word_frequency import histogram
from dictionary_sentence import read_text_file, list_convert

def random_word(histogram):
    '''Takes in histogram and returns a random word'''
    rand_word = random.choice(list(histogram.keys()))
    return rand_word
    
def choose_sample(storage_list):
    '''creates a dictionary sample using a list'''
    
    list_sample = {}
    
    for word in storage_list: #0(n)
        if list_sample.get(word) is None: #0(1)
            list_sample[word] = 1
        else:
            sample_list[word] += 1
        return list_sample
        
def weighted_choice(histogram):
    '''Returns a word based on its weighted probability by using random.randint'''
    #Converts a list of keys and values
    words, weights = zip(*histogram.items())
    
    weight_list = []  #weight_list
    current_weight = 0 #curr_weight
    for weight in weights:
        current_weight += weight
        weight_list.append(current_weight)
        
    random_num = random.randint(1, current_weight)
    
    for word, weight in zip(words, str(int(current_weight))):
        if random_num <= int(weight):
            return word
            
def test_random(histogram):
    random_list = []
    for i in range (10000):
        njom_list.append(random_word(histogram))
    word_test = choose_sample(random_list)
    print(word_test)
    
def test_random_weight(histogram):
    weighted_words = []
    for i in range(10000):
        random_word = weighted_choice(histogram)
        weighted_words.append(random_word)
    weighted_word = choose_sample(weighted_word)
    print(weighted_words)
    
def main():
    '''reads in histogram and returns random word'''
    txt = read_text_file('fish.txt') 
    text_list = list_convert(text)
    
    my_histogram = histogram(text_list)
    
    test_random(my_histogram)
    test_random_weight(my_histogram)
    
if __name__ == '__main__':
    main()

# 
#     def contains(item):
#         for word in word_list:
#             if item == word:
#                 return True
#         return False
# 
# 
# for self in self.buckets
# 
#     top one already loops through what the bottom one is looping through.
# 
        