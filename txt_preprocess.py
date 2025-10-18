import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
import nltk

try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')

def transform_txt(txt):
    txt = re.sub(r'http\S+|www\S+|https\S+', '', txt, flags = re.MULTILINE)
    
    txt = re.sub(r'@\w+', '', txt)
    txt = re.sub(r'#', '', txt)
    
    tokens = re.findall(r'\b\w+\b', txt.lower()) # tokenize
    result = [ps.stem(token) for token in tokens if token not in stop_words] 
    
    return " ".join(result)

