import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def transform_txt(txt):
    txt = re.sub(r'http\S+|www\S+|https\S+', '', txt, flags = re.MULTILINE)
    
    txt = re.sub(r'@\w+', '', txt)
    txt = re.sub(r'#', '', txt)
    
    tokens = re.findall(r'\b\w+\b', txt.lower()) # tokenize
    result = [ps.stem(token) for token in tokens if token not in stop_words] 
    
    return " ".join(result)

