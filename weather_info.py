import requests
import re
pattern="^\d{6}$"
pattern1="[a-z A-Z]"
pincode=input("enter your pincode/Cityname  :")

if(re.search(pattern,pincode)):
    url = "http://api.openweathermap.org/data/2.5/weather?zip=" + pincode + ",in&appid=d556e008e55ad5e65918a1f441b101a9"
    res = requests.get(url).json()
    area = res['name']
    feels_like = str(res["main"]['feels_like'])+"\N{DEGREE SIGN}c"
    temp =str(res["main"]['temp']) +"\N{DEGREE SIGN}c"
    cloud = res["weather"][0]['description']
    pressure = str((res["main"]['pressure'])/1000)+"Bar"
    humidity = str(res["main"]['humidity'])+"%"
    wind =str((res["wind"]["speed"])*3.6)+"km/hr"
    degree = "\N{DEGREE SIGN}c"
    print("location                     :", area)
    print("Feels Like                   :", feels_like)
    print("Cloud Condition              :", cloud)
    print("temprature                   :", temp)
    print("Pressure                     :",pressure)
    print("Humidity                     :",humidity)
    print("Wind Speed                   :",wind)

elif(re.search(pattern1,pincode)):
    url="http://api.openweathermap.org/data/2.5/weather?q="+pincode+ ",in&appid=d556e008e55ad5e65918a1f441b101a9"
    res = requests.get(url).json()
    area = res['name']
    feels_like = str(res["main"]['feels_like']) + "\N{DEGREE SIGN}c"
    temp = str(res["main"]['temp']) + "\N{DEGREE SIGN}c"
    cloud = res["weather"][0]['description']
    pressure = str((res["main"]['pressure']) / 1000) + "Bar"
    humidity = str(res["main"]['humidity']) + "%"
    wind = str((res["wind"]["speed"]) * 3.6) + "km/hr"
    degree = "\N{DEGREE SIGN}c"
    print("location                     :", area)
    print("Feels Like                   :", feels_like)
    print("Cloud Condition              :", cloud)
    print("temprature                   :", temp)
    print("Pressure                     :", pressure)
    print("Humidity                     :", humidity)
    print("Wind Speed                   :", wind)
else:
    print("Ooooop's You Entered Something Wrong")