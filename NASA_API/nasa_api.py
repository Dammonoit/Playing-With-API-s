import requests
import webbrowser
api_address='https://api.nasa.gov/planetary/earth/imagery/?date=2014-02-01&cloud_score=True&api_key=92feVMVIDJVii3BcMqqu9CC58nc5YU8ebZkeOY78&'
#lon=72.5713621&lat=23.022505 is for ahmedabad
lat=input('Enter The Latitute of the place you wanna see: ')
lon=input('Enter The Longitude of the place you wanna see: ')
lat1='lat='+lat
lon1='lon='+lon
url=api_address+lon1+'&'+lat1
json_data = requests.get(url).json()
print('opening the jason data in new tab in browser.');print('\n')
webbrowser.open_new_tab(url)
url_output=json_data['url']
print(url_output);print('\n')
print('Now taking you the url or NASA image.')
webbrowser.open_new_tab(url_output)

