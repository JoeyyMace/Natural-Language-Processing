import re
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Load English tokenizer/lemmatizer
nlp = spacy.load("en_core_web_sm")
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download('punkt_tab')

#setup
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

def clean_text(text, use_lemmatizer=True, use_stemmer=False):
    #1. Lowercase
    text = text.lower()
    
    #2. Remove puncuation and numbers
    text = re.sub(r"[^a-z\s]", "", text)
    
    #3. Tokenize
    tokens = nltk.word_tokenize(text)
    
    #4 Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    
    #5 Lemmatize or Stem
    if use_lemmatizer:
        doc = nlp(" ".join(tokens))
        tokens = [token.lemma_ for token in doc]
    elif use_stemmer:
        tokens = [stemmer.stem(word) for word in tokens]
        
    return tokens


#Take input
n = input("Please enter a phrase: ")
cleaned = clean_text(n) #Output all of the key words in the phrase
print(cleaned)
