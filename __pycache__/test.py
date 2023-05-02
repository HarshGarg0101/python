from wordcount import  word_frequency

url = 'https://en.wikipedia.org/wiki/Stealth_startup'
word_counts = word_frequency(url)

print(word_counts)