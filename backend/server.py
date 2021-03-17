from flask import Flask, request,render_template,url_for,redirect
from flask_cors import CORS, cross_origin
from datetime import datetime
import json 
import requests


f = open('data.txt') 
data = json.load(f) 

ff = open('cities.txt') 
cities = json.load(ff) 

fff = open('countries.txt') 
countries = json.load(fff) 


app=Flask(__name__)
cors = CORS(app)

@app.route('/login',methods = ["POST"])
@cross_origin()
def LOGIN():
    name=request.form.get("name")
    passw=request.form.get("passw")
    if name=='mamak' and passw=='9a7ba':
        return 'oki'
    return 'nope'

days={'1':'Monday', '2':'Tuesday', '3':'Wednesday', '4':'Thursday', '5':'Friday', '6':'Saturday' ,'7': 'Sunday'  }

@app.route('/minute',methods = ["POST"])
@cross_origin()
def min():
    city=request.form.get("chosencity")
    country=request.form.get("chosencountry")
    r=requests.get('https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid=841ca126c041f663380a01a7771efca3'.format(data[country][city]["coord"]["lat"],data[country][city]["coord"]["lon"]))
    a=r.json()
    temp={}
    pressure={}
    humidity={}
    clouds={}
    wind_speed={}
    wind_deg={}
    weather_description={}
    for i in range (len(a["hourly"])):
        temp.update({i:round(a["hourly"][i]['temp']-273.15, 1)})
        humidity.update({i:a["hourly"][i]['humidity']})
        clouds.update({i:a["hourly"][i]['clouds']})
        wind_speed.update({i:round(a["hourly"][i]['wind_speed']*3.6, 1)})
        weather_description.update({i:a["hourly"][i]['weather'][0]['description']})
    sunrise={}
    sunset={}
    temp_day={}
    temp_night={}
    temp_min={}
    temp_max={}
    pressure={}
    hum={}
    cloud={}
    wind_sp={}
    weather={}
    lst=[]
    for i in range (len(a["daily"])):
        day=days[datetime.fromtimestamp(a["daily"][i]['dt']).strftime('%u')]
        lst.append({'name':i,'day':day,'sunrise':a["daily"][i]['sunrise'],'sunset':a["daily"][i]['sunset'],'temp_min':round(a["daily"][i]['temp']['min']-273.15,1),'temp_max':round(a["daily"][i]['temp']['max']-273.15,1),'hum':a["daily"][i]['humidity'],
        'cloud':a["daily"][i]['clouds'],'wind_sp':round(a["daily"][i]['wind_speed']*3.6, 1),'weather':a["daily"][i]['weather'][0]['description']})
    r=requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid=841ca126c041f663380a01a7771efca3'.format(city))
    dt=r.json()
    dt['main']['temp']=round(dt['main']['temp']-273.15,1)
    dt['sys']['sunrise']=datetime.fromtimestamp(dt['sys']['sunrise']).strftime('%m/%d/%Y, %H:%M:%S')
    dt['sys']['sunset']=datetime.fromtimestamp(dt['sys']['sunset']).strftime('%m/%d/%Y, %H:%M:%S')    
    return json.dumps([lst,{'temp':temp,'pressure':pressure,'humidity':humidity,'clouds':clouds,'wind_speed':wind_speed,'wind_deg':wind_deg,'weather_description':weather_description},dt])  




@app.route('/country',methods = ["POST"])
@cross_origin()
def countryname():
    return json.dumps(countries)


@app.route('/city',methods = ["POST"])
@cross_origin()
def cityname():
    country=request.form.get("chosencountry")
    return json.dumps(cities[country])



if __name__=="__main__":
    app.run(debug=True,port=5000)


