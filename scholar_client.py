"""
Script to get h-index, i-index, and recent publications for desired researchers.
This is the updated code that will use the most recent version of scholarly. That is version 1.2.0
This scrip is the 'client' and will be the code that we will aim to have researchers interact with.
"""

#Edit the file name to specify where the retrieved information will save too.
fname = 'google_scholar_data_names.csv'


# !pip install scholarly==1.2.0
from google_scholarly_updated import scholar_search
from google_scholarly_updated import pull_names
from google_scholarly_updated import append_method
from scholarly import scholarly

author_names = pull_names(fname)
fname = append_method(fname)

scholar_search(fname,author_names,'three recent')
