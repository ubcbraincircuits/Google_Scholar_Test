"""
Script to get h-index, i-index, and recent publications for desired researchers.
This is the updated code that will use the most recent version of scholarly. That is version 1.2.0
"""
#!pip install scholarly
import csv

def append_method(fname):
  new_name = ""
  list_of_file = list(fname)
  for item in list_of_file:
      if (item == '.'):
          break
      new_name = new_name + item

  new_name = new_name +'_output.csv'
  return new_name

def pull_names(fname):
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
            author_names[i]=row[0]
            i = i +1

  return author_names



def scholar_search(fname,author_names,m_name):

  if (m_name == "indicies"):
    index_method(fname,author_names)
    return
  if (m_name == "three recent"):
    three_recent_method(fname, author_names)
    return
  else:
    print("error")

# index_method tales uses the parameter and outputs the three most recent publications by the authors sepcified
# using the google scholarly API. It also retrieves the hindex, hindex5, i10index and i10index5. 
# It then puts all these things into a csv file, using the name passed to it via the 'client' file.
# 
# inputs: filename (string), author_names(array of strings)
# outputs: csv file saved in the same directory with filename
def index_method(fname,author_names):

  #importing proper packages
  #reminder to pip install scholarly before running this code
  from scholarly import scholarly
  import csv

  query_row = ['Name', 'H Index', 'H Index 5 years', 'I Index', 'I Index 5 years']

  # This creates/opens the file with filename with the intention to write to the csv_file
  # The encoding allows the characters to be properly written to the csv_file
  with open(fname, mode='w', encoding ="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(query_row)

    # For loop goes for the length of authors in the array and performs the follwoing task with each author
    for author_string in author_names:

      # Perferms the search for the indices of the author, hindex....
      search_query = scholarly.search_author(author_string)
      #search_query = scholarly.search_author(author_string[0])

      try :
        author = next(search_query)
      except (RuntimeError,TypeError,StopIteration):
        row = [author_string,'no information found']# + recent_pubs
        csv_writer.writerow(row)
      
        
      
      objref = scholarly.fill(author, sections=['indices'])

      hindex = objref.get("hindex")
      hindex5 = objref.get("hindex5y")
      i10index = author.get("i10index")
      i10index5 = author.get("i10index5y")

      # Write them to the csv file
      row = [author_string,hindex,hindex5,i10index,i10index5]
      csv_writer.writerow(row)

# index_method tales uses the parameter and outputs the three most recent publications by the authors sepcified
# using the google scholarly API. 
# It then puts all these things into a csv file, using the name passed to it via the 'client' file.
# 
# inputs: filename (string), author_names(array of strings)
# outputs: csv file saved in the same directory with filename
def three_recent_method(fname,author_names):

  #importing proper packages
  #reminder to pip install scholarly before running this code
  from scholarly import scholarly
  import csv

  query_row = ['Name', 'Pub 1','Pub 2','Pub 3']

  # This creates/opens the file with filename with the intention to write to the csv_file
  # The encoding allows the characters to be properly written to the csv_file
  with open(fname, mode='w', encoding ="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(query_row)

    # For loop goes for the length of authors in the array and performs the follwoing task with each author
    for author_string in author_names:

      # Perferms the search for the indices of the author, hindex....
      search_query = scholarly.search_author(author_string)
      author = next(search_query)

      pubs = scholarly.fill(author, sections=['publications'])
      
      # Intialize the dictonary
      dict1 = {}

      # For the amount of publications per author, write the year and title to the dictionary 
      for pub in author['publications']:
        # Only include publications that have a documented year of publishing
        if 'pub_year' in pub['bib']:
          year_pub = pub['bib']['pub_year']
          title_pub = pub['bib']['title']

          # Write these to the dictionary using the title as the key to avoid repeats of keys
          dict1[title_pub] = year_pub


      # Sort the dictionary by year in order to have the most recent publications at the top
      # Note since this is only done by year, it can not get down to say month or date of publication
      sort_dict = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
      
      # Only take the three most recent
      recent_pubs = sort_dict[0:3]

      # Write them to the csv file
      row = [author_string] + recent_pubs
      csv_writer.writerow(row)
