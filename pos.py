import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
sentence="Nandita is a student of b.tech 8th semester student. She stay in guwahati. She study in SITM. Doreen and Nandita are classmates."
word=word_tokenize(sentence)
pos_tag=nltk.pos_tag(word)
print(pos_tag)