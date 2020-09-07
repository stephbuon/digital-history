import nltk, numpy, re, matplotlib, num2words, pandas, scipy, numpy as np
from scipy.stats import norm
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# The data can be downloaded in Plain Text UTF-8 from Project Gutenberg:
# Emma https://www.gutenberg.org/files/158/158-0.txt
# Pride and Prejudice https://www.gutenberg.org/cache/epub/42671/pg42671.txt
# Sense and Sensibility https://www.gutenberg.org/cache/epub/21839/pg21839.txt

# Read in the data. Specify "utf8 encoding" for Windows computers. Aren also had some extra problem
# with punctuation but resolved it by replacing substituting apostrophes, I believe. 
with open('sense.txt', 'r', encoding="utf8") as myfile:
    sas_data = myfile.read().split('\n\n"I suppose you know, ma\'am, that Mr. Ferrars is married"\n\nIt _was_ Edward\n\n"Everything in such respectable condition"\n\n ')[1].split('THE END')[0].strip()

with open('emma.txt', 'r', encoding ="utf8") as myfile:
    emma_data = myfile.read().split('CHAPTER I')[1].split('FINIS')[0].strip()

with open('pride.txt', 'r', encoding="utf8") as myfile:
    pap_data = myfile.read().split('CHAPTER I')[1].split('End of the Project Gutenberg EBook of Pride and Prejudice, by Jane Austen')[0].strip()

# Combine the data in a single variable.
data = [sas_data, emma_data, pap_data]

# Now we begin the SciKitLearn-based code. Content warning: sci-kit learn's documentation went through a blender
# before publication. 

# initalize CountVectorizer()
cv=CountVectorizer(stop_words='english')

# return word counts for the words in data
word_count_vector=cv.fit_transform(data)

# view the "vocabulary words," or tokens, in the data
# According to Jo's notes, the numbers next to the tokens are their indices, not the word counts.
cv.vocabulary_

# create a varaible that contains the sum of each word occurence in all books (i.e. Sense and Senability, Emma, etc.) 
sum_words = word_count_vector.sum(axis=0)

# sort the list of tuples that contain the word and their occurence in the corpus.
words_freq = [(word, sum_words[0, idx]) for word, idx in cv.vocabulary_.items()]

words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)

# review output by displaying the top 10
words_freq[:10]

# use tfidf_transformer.fit on the variable we defined earlier, word_count_vector.
# tfidf_transformer transforms a count matrix to a normalized TF or TF-IDF representation
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)

tfidf_transformer.fit(word_count_vector)

# Review IDF values. The output data frame has the token and the IDF weight. It's weird (to me) that the 
# token is the index, however.
df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(),columns=["idf_weights"])

# Compute the TF-IDF scores (these are not Jo's custom TF-IDF measures, by the way, Aren)
tf_idf_vector=tfidf_transformer.transform(word_count_vector)

# Now Jo creates a DF with token (as index) and TF-IDF score as a regular column.
feature_names = cv.get_feature_names()

first_document_vector=tf_idf_vector[0]

# Show the frist ten scores for the frist document in the data (Sense and Sensability)
df = pd.DataFrame(first_document_vector.T.todense(), index=feature_names, columns=["tfidf"])
df.sort_values(by=["tfidf"],ascending=False).head(10)

# the above process can also be completed in one step. Below is sci-kit learn's all-in-one TF-IDF vectorizor
from sklearn.feature_extraction.text import TfidfVectorizer 
 
# Set the parameters in which the sci-kit learn TF-IDF vectorizor will operate
tfidf_vectorizer = TfidfVectorizer(stop_words='english', use_idf=True)

# use the vectorizor 
tfidf_vectorizer_vectors=tfidf_vectorizer.fit_transform(data)

# Calculate the log-liklihood of each word
LL_score = scipy.stats.norm.pdf(word_count_vector.data)

### Here is where we get stuck in murkey water. Jo wants a DF with two columns: one for token and one for log-liklihood
### score. Steph thought she could make this DF by joining the tokens from cv.vocabulary_ to the log-liklihood scores in 
### LL_score.

# The following code makes two DFs: one for the tokens and one for the LL score.
vocab_DF = pd.DataFrame.from_dict(list(cv.vocabulary_))

LL_DF = pd.DataFrame(LL_score)

# Before joining them, however, Steph saw that the lengths of each DF was different:

len(cv.vocabulary_) # returns 1119

len(LL_DF) # returns 1215 

#### we have a problem: why aren't these arrays the same length? 
