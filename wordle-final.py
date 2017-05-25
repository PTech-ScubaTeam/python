#Import the string package - some nice functions to remove punctuation
import string

#List of stopwords
stopwords=['ah','about','at','when','without','its','since','has','if','way','into','it','on','for','to','is','was','any','so','of','as','and','or','but','are','the','a','that','they','in','our','then','their','am','also','yet','not','very','we','after','do','this','have','been','he','know','some','him','her','what','can','just','an','why','where','with','it\'s','oh','here','which','other','did','than','even','ever','very','get','like','there','by','from','one','even','though','no','had','be','ok','because','might','much','too','them','such','these']


#Word List
words = []

#Word frequency dictionary ( will have word and # of times it appears)
frequency_dictionary = {}
#Open the file in READ mode 'r'
f =  open('declaration.txt','r')

#Read each line one at a time
for line in f.readlines():
    #strip the line (remove trailing newlines) and
    #split it up into words which are separated by spaces usually
    #parssed_words is now a list of words ["each","man"]
    parsed_words = line.strip().split(' ')

    #now we need to normalize (remove punctuation & lowercase)
    #and remove them if they are stopwords

    for word in parsed_words:
        lowercase_word = word.lower().strip( string.punctuation)

	   #Add to the list of words now
        if lowercase_word not in stopwords and len(lowercase_word) > 0:
            words.append( lowercase_word)

words.sort()

#Go through the list and add them to the dictionary.
for w in words:
    if w not in frequency_dictionary:
        frequency_dictionary[w] = 1
    else:
        frequency_dictionary[w] = frequency_dictionary[w] + 1

f.close()
#print frequency_dictionary


#We could have also only printed out words that appear more than 2 times:
for word,freq in frequency_dictionary.items():
    if freq > 2:
        print '<span class="level-' + str(freq) + ' rotate">' + word + '</span>'
