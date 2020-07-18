from pynytimes import NYTAPI
import datetime

#INIT
nyt = NYTAPI("Your API Key")

#Search for articles
articles = nyt.article_search(query = "Indigo")

#Open file in writing mode
file = open("Result_URL(s).txt", 'w')

#write these urls into a file
for i in range(len(articles)):
	file.write(articles[i]['web_url'] + '\n')
	
#file close
file.close()
