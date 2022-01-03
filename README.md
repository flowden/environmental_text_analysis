# environmental_text_analysis
# General description:
  For my PLCY honors thesis, I conducted a text analysis project to understand how corporate
philanthropy affects environmental nonprofit discourse. I constructed a text database
that contained 228 annual reports published by 10 environmental movement organizations
from 1980 through 2020. I then built my own dictionaries that indicate rhetoric meant to
slow climate action and used dictionary methods to measure the prevalence of delay rhetoric
in my text database on an annual basis. I then used this novel text data with data
from a corporate philanthropy database in a series of fixed effects regressions to explore
how corporate giving can affect environmental nonprofit discourse.

# Individual file description
1. Dictionary methods
  I apply my novel dictionaries to my corpus of annual reports. I use Anaconda and Jupyter Notebook
for this project along with the Pandas and Natural Language Toolkit (NLTK) modules. First, I import
my text data from google sheets. Second, I clean my text data by removing stop words and punctuation.
I then apply created dictionaries to my texts to measure how often words in my dictionaries appear
in documents in my corpus. I then export this data as an Excel spreadsheet for data visualization.
  Dictionary-based methods are advanced word counting techniques that can measure the prevalence of
certain words and phrases in a corpus. Scholars, researchers, or other individuals first identify
words and terms that are indicative of certain themes they expect to find in their corpus. The
collection of words is referred to as a ‘dictionary.’ Using the Python programming language or
many others, researchers then write code to count how often each word in their dictionary appears
in each document of their corpus. These word counts are recorded and then converted into percentages
that can be used in later analysis or displayed in charts, graphs, and tables to communicate a
researcher’s findings. 

2. MA_CT_opposition_testimony
  I conduct a robustness check on my created dictionaries by running them on texts where I expect
delay rhetoric to be prominent. I follow the same process as outlined above by applying my dictionaries to
this separate corpus of statehouse testimony in Massachusetts and Connecticut.
  
3. Word_frequency
  I find the most frequently used words in the statehouse testimony in Massachusetts and Connecticut. I used this
data to ensure there were no commonly-used words in this data that should have been included in my dictionaries.
  
4. XLSX_to_TXT
  This code converts rows of my text database into individual txt files that are needed to conduct topic modeling
on my corpus using Mallet. I could have stored all of my collected texts in individual text files; however, storing
them in a spreadsheet allowed me to collect additional metadata (e.g., group name, year, type of text, source, etc.)
that can be useful in certain applications of topic modeling, such as structural topic modeling. Automating this
conversation of spreadsheet rows to text files created 3029 txt files in seconds. 
