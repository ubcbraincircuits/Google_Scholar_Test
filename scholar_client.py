"""
Script to get h-index, i-index, and recent publications for desired researchers.
This is the updated code that will use the most recent version of scholarly. That is version 1.2.0
This scrip is the 'client' and will be the code that we will aim to have researchers interact with.
"""

#Edit the file name to specify where the retrieved information from. 
fname = 'google_scholar_data_names.csv'

"""
Edit this info_selection array to include 1 to include the information in the output. Note, the names will always be printed.
The name that will be printed in the one that is found on Google Scholar
a[0]: Affiliations
a[1]: Indicies
a[2]: Interests
a[3]: Citations
a[4]: 3 Most Recent Publications
"""
info_selection = [1,0, 0, 1, 0]

# !pip install scholarly
from google_scholarly_updated import scholar_search, append_method
import csv
import os 

j = 0

with open(fname, encoding ="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =',')
    for row in csv_reader:
     j = j +1

author_names= ['0']*j

i = 0


with open(fname, encoding ="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =',')
    for row in csv_reader:
        if (len(row) == 1):
            author_names[i]=row
            i = i +1


fname = append_method(fname)

scholar_search(fname,author_names,info_selection)
