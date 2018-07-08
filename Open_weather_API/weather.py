import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=aa53dd83a55493dfb04245c922bfc78c&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
main = json_data['weather'][0]['main']
humidity = json_data['main']['humidity']
temperature = json_data['main']['temp']
print('humidity: ',humidity)
print('temperature: ',temperature)
print('main: ',main)



