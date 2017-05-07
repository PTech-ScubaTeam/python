#Import the string package - some nice functions to remove punctuation
import string

#List of stopwords
stopwords=['ah','about','at','when','without','its','since','has','if','way','into','it','on','for','to','is','was','any','so','of','as','and','or','but','are','the','a','that','they','in','our','then','their','am','also','yet','not','very','we','after','do','this','have','been','he','know','some','him','her','what','can','just','an','why','where','with','it\'s','oh','here','which','other','did','than','even','ever','very','get','like','there','by','from','one','even','though','no','had','be','ok','because','might','much','too','them','such','these']


#Word List
words = []

#Word frequency dictionary ( will have word and # of times it appears)
frequency_dictionary = {}
#Open the file in READ mode 'r'
