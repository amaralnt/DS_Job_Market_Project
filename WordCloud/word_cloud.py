import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
os.chdir(sys.path[0])

# Read text
text = open('job_titles.txt', mode='r', encoding='utf-8').read()
stopwords = STOPWORDS

wc = WordCloud(
    background_color='black',
    stopwords=stopwords,
    height=600,
    width=1200,
    max_words=50,
    max_font_size=150,
    random_state=88
)

wc.generate(text)

# Store to file
wc.to_file('wordcloud_output.png')