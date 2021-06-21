import requests

from datetime import datetime

api_key = '1cc89089ee4169641fac7a0703ae9e9a'
location = input("Enter the city name: ").lower()

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

s="-------------------------------------------------------------"
s1="Weather Report for - {}  || {}".format(location.upper(), date_time)

s2="Current temperature is: {:.2f} deg C".format(temp_city)
s3="Current weather desc  : {}".format(weather_desc)
s4="Current Humidity      : {} %".format(hmdt)
s5="Current wind speed    : {} coikmph".format(wind_spd) 
print(s, "\n", s1, "\n", s, "\n", s2, "\n", s3, "\n", s4, "\n", s5, "\n")
with open ("Weather.txt","a+") as weather:
    weather.writelines(s+"\n")
    weather.writelines(s1+"\n")
    weather.writelines(s+"\n")
    weather.writelines(s2+"\n")
    weather.writelines(s3+"\n")
    weather.writelines(s4+"\n")
    weather.writelines(s5+"\n\n")