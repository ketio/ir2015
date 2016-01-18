from porter2 import stem
import stopWords

# return a "list" of terms in the document (depulicate will not be removed) 
def terms_extracter(file_name):

	#open document
	f = open(file_name,"r")

	#read text from document
	data = f.read()

	replace_chars = "1234567890;:,.`~!@#$%^&*-_+=()[]{}|`'/\"\\?"

	#replace some non-alphabetic characters with space
	for i in replace_chars:
		data = data.replace(i," ")

	#Tokenization
	token = data.split()

	#Lowercasing everything
	lowerToken = map(lambda x:x.lower(), token)

	#Stemming using Porters algorithm
	porters = map(lambda x: stem(x), lowerToken)

	#Stopword removal
	result = stopWords.rmStopWords(porters)

	return result