from operator import truediv
import re
import string
import math

TEXT_TO_MINE = "Alicia.txt"
STOPWORDS = "stopwords.txt"

def open_file(file_path):
    # opening the file in read mode
    my_file = open(file_path, encoding="utf-8")
  
    # reading the file
    data_from_file = my_file.read()
    return data_from_file

def sanitize_data_from_file(data_from_file):  
    # replacing end of line('/n') with ' ' and
    # splitting the text it further when '.' is seen.
    data_into_list = data_from_file.replace('\n', ' ')
    data_into_list2 = data_into_list.replace('—', ' ').split(" ")
    return data_into_list2

'''
Finally we won't use these two methods because we created another one which does the same

def remove_punctuation(word):
    return re.sub("[.|,|;|:|!|?|(|)|-|_]", "", word)

def remove_apostrophe(word):
    return word.replace("'s", "")
'''

def remove_suffix(word):
    #removing the puntcuation symbols and every charcater after them and returning the word in lowercase
    word_aux = re.sub("[(.|,|;|:|!|?|(|)|_|’|')][^*]+$", "", word)
    word_aux2 = re.sub("[^\w\s]", "", word_aux)

    return word_aux2.lower()

def normalize(sanitized_data_from_file):
    #create a list with the sanitized words without punctuation and unwanted parts
    normalized_data = list(map(remove_suffix, sanitized_data_from_file))

    normalized_data = list(filter(None, normalized_data))

    return normalized_data

def is_included_in_stopwords(word, stopwords_set):
    #returns True if the stopword is not included in the Alice text (to filter the text in the next method)
    if word in stopwords_set:
        return False
    else:
        return True

def remove_stopwords(sanitized_data_from_file, stopwords_set):
    #remove the stopwords from the text usind filter function
    alice_without_stopwords = list(filter(lambda word: is_included_in_stopwords(word, stopwords_set), sanitized_data_from_file))
    return alice_without_stopwords

def count_words(normalized_data):
    #getting the word count for each word in the text
    word_dict = {}
    for word in normalized_data:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def get_probability(word_count, total_words):
    #getting the probability in % of each word in the text
    return (word_count[0], round(word_count[1] / total_words * 100, 2))

def word_probability(word_dict):
    #creating a dictionary with each word as a key and the probability in % as the value
    len_aux = len(word_dict)
    prob_dict = dict(map(lambda word_value: get_probability(word_value, len_aux), word_dict.items()))
    return prob_dict
   
def get_hist(prob_count):
    #getting the frecuency of each word in # (if the word has a 100% of probability to appear in the text, it has 50 #)
    return (prob_count[0], math.ceil(prob_count[1] / 2) * '#')
       
def display_histogram(prob_dict):
    #print each word with its number of # in a different line (display the histogram)
    histogram = dict(map(get_hist, prob_dict.items()))  
    for k, v in histogram.items():
        print(k,':', v)