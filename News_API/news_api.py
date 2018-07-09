import webbrowser
import json
import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=77d5876cf16548079fc6e0f931a0070e')
response = requests.get(url)
print('The response URL is: ',response.content);print('\n')
#webbrowser.open_new_tab(response)
json_data=response.json()
print ('JASON data is : \n',json_data)
status=json_data['status']
#now we'll print all the news sources.
l=list() #this is a list of all the news sources.
for i in range(0,len(json_data['articles'])):
    l.append(json_data['articles'][i]['source']['name'])
print(l)
#now let's store all the headlines.
title=list()
for i in range(0,len(json_data['articles'])):
    title.append(json_data['articles'][i]['title'])
#also let's store all the url.
url=list()
for i in range(0,len(json_data['articles'])):
    url.append(json_data['articles'][i]['url'])
print(title)
print(url)

#########################################################
#now let's search news article for specific topic or keyword.
query=input('Enter you query: ')  #for eg: apple
final_url='https://newsapi.org/v2/everything?'+'q='+query+'&apiKey=77d5876cf16548079fc6e0f931a0070e'
print(final_url)
response_new = requests.get(final_url)
json_data_new=response_new.json()
print (json_data_new)
