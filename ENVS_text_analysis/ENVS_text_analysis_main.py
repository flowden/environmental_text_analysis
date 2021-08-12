python get-pip.py
import pandas as pd

# Importing datasets
NTEE_codes = pd.read_csv(r'/Users/finn/Dropbox/CDL/Thesis/Datasets/BusinessMasterFile.csv')
Trade_found = pd.read_csv(r'/Users/finn/Dropbox/CDL/Thesis/Datasets/NTEE_Codes.xlsx')

#code
print(NTEE_codes)
