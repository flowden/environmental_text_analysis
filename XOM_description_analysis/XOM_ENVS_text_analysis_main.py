# Modules
import pandas as pd
import nltk

# set screen display options
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

# file names
data_file = '/Users/klowden/Dropbox/Brown 2021-2022/THESIS/' \
            'Python/XOM_descriptions_data/XOM_descriptions_ENVS_groups.xlsx'

# read in the data
df = pd.read_excel(data_file, sheet_name=0, header=0)

# Casting Description as text
convert_dict = {'Description': str}
df = df.astype(convert_dict)

# Grabbing first row of description column
# text = df.loc[1, "Description"]

# Mapping all text from description column into one string
text = df.Description.str.cat(sep=' ')

# word tokenization
from nltk.tokenize import word_tokenize

tokenized_words = word_tokenize(text)
# print(tokenized_word)


# Removing stopwords
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
stop_words.update("For", "$", ":", ",")
filtered_sent = []

for w in tokenized_words:
    if w not in stop_words:
        filtered_sent.append(w)

# Frequency distribution
from nltk.probability import FreqDist

fdist = FreqDist(filtered_sent)
print(fdist.most_common(10))  # Prints the 10 most-common words
