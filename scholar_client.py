"""
Script to get h-index, i-index, and recent publications for desired researchers.
This is the updated code that will use the most recent version of scholarly. That is version 1.2.0
This scrip is the 'client' and will be the code that we will aim to have researchers interact with.
"""

#Edit the file name to specify where the retrieved information will save too.
fname = 'google_scholar_data_test7.csv'

#Edit this array with names of the researchers in which you are looking to retreve information on
author_names = ['Brian MacVicar', 'Jeffrey LeDue', 'Tim H. Muprhy', 'Tim Murphry']

from google_scholarly_updated import scholar_search

scholar_search(fname,author_names,'indicies')
