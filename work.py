import wordcloud
import numpy
import io
import sys
from matplotlib import pyplot as plt

file_contents = open('document.txt').read()

# print(len(f.read()))

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    freq = {}
    uni_words = []

    for letter in punctuations:
        file_contents = file_contents.replace(letter,' ')

    for word in uninteresting_words:
        rem = " " + word + " "
        file_contents = file_contents.replace(rem,' ')

    for word in file_contents.split():
        if word.lower() not in uni_words:
            uni_words.append(word.lower())
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(freq)
    return cloud.to_array()

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
