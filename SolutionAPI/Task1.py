from newsapi import NewsApiClient

# Init
# *******************
# REPLACE unique key WITH YOUR API KEY
# *******************
newsapi = NewsApiClient(api_key = unique key)
print("Select from these two options:"+'\n'+
	"1. Search about a particular topic"+'\n'+
	"2. Get top news from any source")
n = input()

if(int(n) == 1):
	query = input("enter topic")
	choice = input("News from particular date ? Y/N")
	if(choice == "Y"):
		date = input("enter date in the format YYYY-MM-DD")
		try:
			result = newsapi.get_everything(q=query, sort_by= 'relevancy', page_size = 10, from_param = date)
			print(result)
		except:
			print("An error occurred")
	else:
		try:
			result = newsapi.get_everything(q=query, sort_by= 'relevancy', page_size = 10)
			print(result)
		except:
			print("An error occurred")

elif(int(n) == 2):
	source = input("enter a source")
	try:
		result = newsapi.get_top_headlines(sources = source, page_size = 10)
	except:
		print("An error occurred")
else:
	print("Enter valid choice")
