#This Program is for Python 2.7 version
import nltk
import string
import glob
import os
from nltk.tokenize import RegexpTokenizer

outputPath  = ""
fileCnt     = 0
tokenizer   = RegexpTokenizer(r'\w+')
stopWords   = set(nltk.corpus.stopwords.words('english'))
#Customized stop words (lower case)
cuStopWords = {'court','courts','appeals','appeal','federal','circuit','patents','patent','commissioners','commissioner','board','jan','january','february','march','april','may','june','july','august','september','october','november','december'}
for i in cuStopWords:
    stopWords.add(i)

#Porter or Snowball Stemmer
#stemmer    = nltk.stem.porter.PorterStemmer()
stemmer     = nltk.stem.snowball.EnglishStemmer()

# Scan all txt files 
for name in glob.glob('C:\Users\Nancy\Downloads\Data Cleaning\*.txt'):

    fileCnt    = fileCnt + 1 
    file       = open(name,"r")
    base       = os.path.basename(name)
    outputPath = "C:\Users\Nancy\Downloads\Data Cleaning\Stemmed_" + base
    saveFile   = open(outputPath,'a')
    
    for block in file:
      
        #Convert all letters to lower case
        paperListLower = string.lower(block)   

        #Remove the punctuations
        remove_punc = paperListLower.translate(None, string.punctuation)
        remove_punc = remove_punc.translate(None, "0123456789")

        #Tokenize
        tokens = tokenizer.tokenize(remove_punc)        
        
        #Remove stop words
        remove_stop = [words for words in tokens if not words in stopWords]

        #Stemming        
        stemmed = [stemmer.stem(w.decode('utf-8', errors='ignore')) for w in remove_stop]

        #Print stemmed result
        saveFile.write(' '.join(map(str, stemmed))+"\n")
    
file.close()        
print "Total Stemmed " + str(fileCnt) + " files" 
