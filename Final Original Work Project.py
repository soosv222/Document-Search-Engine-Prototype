#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imports
import spacy
from time import time
nlp = spacy.load('en_core_web_lg')


# In[2]:


# Acessing Documents
AI = nlp(open('OWDocuments/ai.txt').read())
Atoms = nlp(open('OWDocuments/atom.txt').read())
Basketball = nlp(open('OWDocuments/basketball.txt').read())
Birds = nlp(open('OWDocuments/birds.txt').read())
Cold_War = nlp(open('OWDocuments/coldwar.txt').read())
Covid_19 = nlp(open('OWDocuments/covid.txt').read())
English = nlp(open('OWDocuments/english.txt').read())
F1 = nlp(open('OWDocuments/f1.txt').read())
Film = nlp(open('OWDocuments/film.txt').read())
Mars = nlp(open('OWDocuments/mars.txt').read())
Middle_Ages = nlp(open('OWDocuments/middle_ages.txt').read())
Milky_Way = nlp(open('OWDocuments/milky_way.txt').read())
Music = nlp(open('OWDocuments/music.txt').read())
NYC = nlp(open('OWDocuments/nyc.txt').read())
Olympics = nlp(open('OWDocuments/olympics.txt').read())
Renaissance = nlp(open('OWDocuments/renaissance.txt').read())
Soccer = nlp(open('OWDocuments/soccer.txt').read())
Texas = nlp(open('OWDocuments/texas.txt').read())
Trees = nlp(open('OWDocuments/trees.txt').read())
USA = nlp(open('OWDocuments/usa.txt').read())
docs = [('Artificial Intelligence',AI),('Atoms',Atoms),('Basketball',Basketball),("Birds",Birds),('Cold War',Cold_War),('Covid-19',Covid_19),('English',English),('Formula 1',F1),('Film',Film),('Mars',Mars),('The Middle Ages',Middle_Ages),('The Milky Way Galaxy',Milky_Way),('Music',Music),('New York City',NYC),('Olympics',Olympics),('Renaissance',Renaissance),('Soccer',Soccer),('Texas',Texas),('Trees',Trees),('United States of America',USA)]


# In[3]:


def process_doc(doc):
    processed_text = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    doc = nlp(" ".join(processed_text))
    return doc


# In[4]:


def search_results(search_doc):
    result1 = None
    result2 = None
    result3 = None
    title1 = None
    title2 = None
    title3 = None
    for doc in docs:
        similarity = search_doc.similarity(doc[1])
        if result1 == None or similarity>search_doc.similarity(result1):
            result1, result2, result3 = doc[1], result1, result2
            title1, title2, title3 = doc[0], title1, title2
        elif result2 == None or similarity>search_doc.similarity(result2):
            result2, result3 = doc[1], result2
            title2, title3 = doc[0], title2
        elif result3 == None or similarity>search_doc.similarity(result3):
            result3 = doc[1]
            title3 = doc[0]
    return [(title1, title2, title3),(result1, result2, result3)]


# In[5]:


temp_docs = [(tpl[0],process_doc(tpl[1])) for tpl in docs]


# In[ ]:


search_text = input("Search: ")
start = time()
print("Searching...\n\n")
search_doc = nlp(search_text)
results = search_results(search_doc)
print("Top Results:\n\n")
for i in range(len(results[0])):
    print(results[0][i],"\nRelevancy Score:",search_doc.similarity(results[1][i]),"\n\n")
    print(results[1][i],"\n\n")
end = time()
print('Search Time:',round(end-start,2),'seconds')

