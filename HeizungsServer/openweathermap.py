##
## WeatherBinding for openweathermap.org Mathias Aschhoff 2018
##

import requests
import datetime
import logging

def init():
    logging.basicConfig(filename='openwheatermap.log',level=logging.DEBUG)
    logging.info("Init() Openwheatermap...")
    #Request openweathermap API
    r=requests.get("http://api.openweathermap.org/data/2.5/weather?q=Holzwickede,de&appid=YOURAPIKEY")
    #get json
    j=r.json()

    #decpde
    temp=j['main']['temp']
    temp_round=round(temp-273)
    humidity=j['main']['humidity']
    wind=j['wind']
    clouds=j['clouds']['all']
    #rain=j['rain']['rain.3h']
    #snwo=j['snow']['snow.3h']
    sr=datetime.datetime.fromtimestamp(int(j['sys']['sunrise'])).strftime('%H')
    ss=datetime.datetime.fromtimestamp(int(j['sys']['sunset'])).strftime('%H')
    srm=datetime.datetime.fromtimestamp(int(j['sys']['sunrise'])).strftime('%M')
    ssm=datetime.datetime.fromtimestamp(int(j['sys']['sunset'])).strftime('%M')
    
    #Stunde aufrunden
    if(int(srm)>30):
        sr=str(int(sr)+1)
    if(int(ssm)>30):
        ss=str(int(ss)+1)

    print("sunrise: "+sr+srm+" sunset: "+ss+ssm+" temp: "+str(temp_round)+"°C humidity: "+str(humidity)+" clouds: "+str(clouds)+"%")

    #an openhab senden
    sendToOpenHAB("Sunrise_Number",sr)
    sendToOpenHAB("Sunset_Number",ss)
    sendToOpenHAB("Temp_Outside_String",str(temp_round)+"°C")
    sendToOpenHAB("Humidity_Outside_String",str(humidity))


def sendToOpenHAB(item,data):
    print("SEND TO OPENHAB - ITEM: "+item+" DATA: "+data)
    logging.info("SEND TO OPENHAB - ITEM: "+item+" DATA: "+data)
    #OpenHAB API aufrufen
    url = "http://10.10.10.4:8080/rest/items/"+item
    #data = str(round(temp,9))
    #data_json = json.dumps(data) # bei json data={"jsondata"} und als response data=data_json
    headers = {'Content-type': 'text/plain'}
    requests.post(url, data=data, headers=headers)

if __name__ == '__main__':
    init()
