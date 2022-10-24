from text_sanitizing import *

alicia = open_file(TEXT_TO_MINE)
stopwords = open_file(STOPWORDS)
stopwords_sanitized = sanitize_data_from_file(stopwords)

stopwords_set = set(stopwords_sanitized)

alicia_sanitized = sanitize_data_from_file(alicia)

alicia_normalized = normalize(alicia_sanitized)

alice_without_stopwords = remove_stopwords(alicia_normalized, stopwords_set)

alice_word_dict = count_words(alice_without_stopwords)

alice_word_prob_dict = word_probability(alice_word_dict)

alice_histogram = display_histogram(alice_word_prob_dict)

print(alice_histogram)