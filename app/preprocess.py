import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')

STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    """Clean text by removing special characters, stopwords, and extra spaces."""
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters
    text = text.lower()                      # Lowercase
    text = " ".join(word for word in text.split() if word not in STOPWORDS)  # Remove stopwords
    return text

def tokenize_text(text):
    """Tokenize the text."""
    return nltk.word_tokenize(text)
