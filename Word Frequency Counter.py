import nltk
import collections
from nltk.tokenize import word_tokenize
from collections import Counter

def word_freq(text):
    #Tokenize text into words
    tokens =word_tokenize(text)
    
    #Noramlize tokens by removing puncuation and switching to lowercase
    words = [word.lower() for word in tokens if word.isalpha()]
    
    #Count word frequency
    freq = Counter(words)
    
    # Sort words by frequency descending
    sorted_freq = freq.most_common()
    
    return sorted_freq

if __name__ == "__main__":
    n = input("Please enter a phrase: ")
    
    frequencies = word_freq(n)
    
    for word, count in frequencies:
        print(f"{word}: {count}")
    
