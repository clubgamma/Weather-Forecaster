from flask import Flask, render_template, request
import os

import requests
app = Flask(__name__)




url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=<YOUR_API_KEY>' #

urlforecast='http://api.openweathermap.org/data/2.5/forecast?q={}&appid=<YOUR_API_KEY>'





@app.route('/',methods=['GET', 'POST'])
def index():
   return render_template("index.html")

@app.route('/city',methods=['GET', 'POST'])
def searchcity():
   CITY=request.form.get('city')
   r = requests.get(url.format(CITY)).json()
   print(CITY)
   print(r)
   weather ={
            'city' : CITY,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']

            
        }
   #return render_template("result.html",)
   return render_template("next.html",weather=weather)


@app.route('/forecast',methods=['GET', 'POST'])
def forecastcity():
   return render_template("forecast.html")


@app.route('/forecastcity',methods=['GET', 'POST'])
def searchcityforecast():
   CITY=request.form.get('city')
   rforecast = requests.get(urlforecast.format(CITY)).json()
   print(CITY)
   
   weatherforecast ={
            'city' : CITY,

            'DateTime0' : rforecast['list'][0]['dt_txt'],
            'temperature0' : rforecast['list'][0]['main']['temp'],
            'feel_temp0'   : rforecast['list'][0]['main']['feels_like'],
            'max_temp0'   : rforecast['list'][0]['main']['temp_max'],
            'min_temp0'   : rforecast['list'][0]['main']['temp_min'],
            'icon0': rforecast['list'][0]['weather'][0]['icon'],

            'DateTime1' : rforecast['list'][1]['dt_txt'],
            'temperature1' : rforecast['list'][1]['main']['temp'],
            'feel_temp1'   : rforecast['list'][1]['main']['feels_like'],
            'max_temp1'   : rforecast['list'][1]['main']['temp_max'],
            'min_temp1'   : rforecast['list'][1]['main']['temp_min'],
            'icon1': rforecast['list'][1]['weather'][0]['icon'],

            
            'DateTime2' : rforecast['list'][2]['dt_txt'],
            'temperature2' : rforecast['list'][2]['main']['temp'],
            'feel_temp2'   : rforecast['list'][2]['main']['feels_like'],
            'max_temp2'   : rforecast['list'][2]['main']['temp_max'],
            'min_temp2'   : rforecast['list'][2]['main']['temp_min'],
            'icon2': rforecast['list'][2]['weather'][0]['icon'],
            
           """ 'DateTime2' : rforecast['list'][2]['dt_txt'],
            'temperature2' : rforecast['list'][2]['main']['temp'],
            'feel_temp2'   : rforecast['list'][2]['main']['feels_like'],
            'max_temp2'   : rforecast['list'][2]['main']['temp_max'],
            'min_temp2'   : rforecast['list'][2]['main']['temp_min'],
            'icon2': rforecast['list'][2]['weather'][0]['icon'], """

            
            'DateTime3' : rforecast['list'][3]['dt_txt'],
            'temperature3' : rforecast['list'][3]['main']['temp'],
            'feel_temp3'   : rforecast['list'][3]['main']['feels_like'],
            'max_temp3'   : rforecast['list'][3]['main']['temp_max'],
            'min_temp3'   : rforecast['list'][3]['main']['temp_min'],
            'icon3': rforecast['list'][3]['weather'][0]['icon'],


            
            'DateTime4' : rforecast['list'][4]['dt_txt'],
            'temperature4' : rforecast['list'][4]['main']['temp'],
            'feel_temp4'   : rforecast['list'][4]['main']['feels_like'],
            'max_temp4'   : rforecast['list'][4]['main']['temp_max'],
            'min_temp4'   : rforecast['list'][4]['main']['temp_min'],
            'icon4': rforecast['list'][4]['weather'][0]['icon'],


            
            'DateTime5' : rforecast['list'][5]['dt_txt'],
            'temperature5' : rforecast['list'][5]['main']['temp'],
            'feel_temp5'   : rforecast['list'][5]['main']['feels_like'],
            'max_temp5'   : rforecast['list'][5]['main']['temp_max'],
            'min_temp5'   : rforecast['list'][5]['main']['temp_min'],
            'icon5': rforecast['list'][5]['weather'][0]['icon'],



            
            'DateTime6' : rforecast['list'][6]['dt_txt'],
            'temperature6' : rforecast['list'][6]['main']['temp'],
            'feel_temp6'   : rforecast['list'][6]['main']['feels_like'],
            'max_temp6'   : rforecast['list'][6]['main']['temp_max'],
            'min_temp6'   : rforecast['list'][6]['main']['temp_min'],
            'icon6': rforecast['list'][6]['weather'][0]['icon'],


            
            'DateTime7' : rforecast['list'][7]['dt_txt'],
            'temperature7' : rforecast['list'][7]['main']['temp'],
            'feel_temp7'   : rforecast['list'][7]['main']['feels_like'],
            'max_temp7'   : rforecast['list'][7]['main']['temp_max'],
            'min_temp7'   : rforecast['list'][7]['main']['temp_min'],
            'icon7': rforecast['list'][7]['weather'][0]['icon'],


            
            'DateTime8' : rforecast['list'][8]['dt_txt'],
            'temperature8' : rforecast['list'][8]['main']['temp'],
            'feel_temp8'   : rforecast['list'][8]['main']['feels_like'],
            'max_temp8'   : rforecast['list'][8]['main']['temp_max'],
            'min_temp8'   : rforecast['list'][8]['main']['temp_min'],
            'icon8': rforecast['list'][8]['weather'][0]['icon'],


            
            'DateTime9' : rforecast['list'][9]['dt_txt'],
            'temperature9' : rforecast['list'][9]['main']['temp'],
            'feel_temp9'   : rforecast['list'][9]['main']['feels_like'],
            'max_temp9'   : rforecast['list'][9]['main']['temp_max'],
            'min_temp9'   : rforecast['list'][9]['main']['temp_min'],
            'icon9': rforecast['list'][9]['weather'][0]['icon'],


            
            'DateTime10' : rforecast['list'][10]['dt_txt'],
            'temperature10' : rforecast['list'][10]['main']['temp'],
            'feel_temp10'   : rforecast['list'][10]['main']['feels_like'],
            'max_temp10'   : rforecast['list'][10]['main']['temp_max'],
            'min_temp10'   : rforecast['list'][10]['main']['temp_min'],
            'icon10': rforecast['list'][10]['weather'][0]['icon'],


            
            'DateTime11' : rforecast['list'][11]['dt_txt'],
            'temperature11' : rforecast['list'][11]['main']['temp'],
            'feel_temp11'   : rforecast['list'][11]['main']['feels_like'],
            'max_temp11'   : rforecast['list'][11]['main']['temp_max'],
            'min_temp11'   : rforecast['list'][11]['main']['temp_min'],
            'icon11': rforecast['list'][11]['weather'][0]['icon'],

            
            'DateTime12' : rforecast['list'][12]['dt_txt'],
            'temperature12' : rforecast['list'][12]['main']['temp'],
            'feel_temp12'   : rforecast['list'][12]['main']['feels_like'],
            'max_temp12'   : rforecast['list'][12]['main']['temp_max'],
            'min_temp12'   : rforecast['list'][12]['main']['temp_min'],
            'icon12': rforecast['list'][12]['weather'][0]['icon'],

            
            'DateTime13' : rforecast['list'][13]['dt_txt'],
            'temperature13' : rforecast['list'][13]['main']['temp'],
            'feel_temp13'   : rforecast['list'][13]['main']['feels_like'],
            'max_temp13'   : rforecast['list'][13]['main']['temp_max'],
            'min_temp13'   : rforecast['list'][13]['main']['temp_min'],
            'icon13': rforecast['list'][13]['weather'][0]['icon'],

            
            'DateTime14' : rforecast['list'][14]['dt_txt'],
            'temperature14' : rforecast['list'][14]['main']['temp'],
            'feel_temp14'   : rforecast['list'][14]['main']['feels_like'],
            'max_temp14'   : rforecast['list'][14]['main']['temp_max'],
            'min_temp14'   : rforecast['list'][14]['main']['temp_min'],
            'icon14': rforecast['list'][14]['weather'][0]['icon'],

            
            'DateTime15' : rforecast['list'][15]['dt_txt'],
            'temperature15' : rforecast['list'][15]['main']['temp'],
            'feel_temp15'   : rforecast['list'][15]['main']['feels_like'],
            'max_temp15'   : rforecast['list'][15]['main']['temp_max'],
            'min_temp15'   : rforecast['list'][15]['main']['temp_min'],
            'icon15': rforecast['list'][15]['weather'][0]['icon'],

            
            'DateTime16' : rforecast['list'][16]['dt_txt'],
            'temperature16' : rforecast['list'][16]['main']['temp'],
            'feel_temp16'   : rforecast['list'][16]['main']['feels_like'],
            'max_temp16'   : rforecast['list'][16]['main']['temp_max'],
            'min_temp16'   : rforecast['list'][16]['main']['temp_min'],
            'icon16': rforecast['list'][16]['weather'][0]['icon'],

            
            'DateTime17' : rforecast['list'][17]['dt_txt'],
            'temperature17' : rforecast['list'][17]['main']['temp'],
            'feel_temp17'   : rforecast['list'][17]['main']['feels_like'],
            'max_temp17'   : rforecast['list'][17]['main']['temp_max'],
            'min_temp17'   : rforecast['list'][17]['main']['temp_min'],
            'icon17': rforecast['list'][17]['weather'][0]['icon'],


            
            'DateTime18' : rforecast['list'][18]['dt_txt'],
            'temperature18' : rforecast['list'][18]['main']['temp'],
            'feel_temp18'   : rforecast['list'][18]['main']['feels_like'],
            'max_temp18'   : rforecast['list'][18]['main']['temp_max'],
            'min_temp18'   : rforecast['list'][18]['main']['temp_min'],
            'icon18': rforecast['list'][18]['weather'][0]['icon'],


            
            'DateTime19' : rforecast['list'][19]['dt_txt'],
            'temperature19' : rforecast['list'][19]['main']['temp'],
            'feel_temp19'   : rforecast['list'][19]['main']['feels_like'],
            'max_temp19'   : rforecast['list'][19]['main']['temp_max'],
            'min_temp19'   : rforecast['list'][19]['main']['temp_min'],
            'icon19': rforecast['list'][19]['weather'][0]['icon'],



            
            'DateTime20' : rforecast['list'][20]['dt_txt'],
            'temperature20' : rforecast['list'][20]['main']['temp'],
            'feel_temp20'   : rforecast['list'][20]['main']['feels_like'],
            'max_temp20'   : rforecast['list'][20]['main']['temp_max'],
            'min_temp20'   : rforecast['list'][20]['main']['temp_min'],
            'icon20': rforecast['list'][20]['weather'][0]['icon'],



            
            'DateTime21' : rforecast['list'][21]['dt_txt'],
            'temperature21' : rforecast['list'][21]['main']['temp'],
            'feel_temp21'   : rforecast['list'][21]['main']['feels_like'],
            'max_temp21'   : rforecast['list'][21]['main']['temp_max'],
            'min_temp21'   : rforecast['list'][21]['main']['temp_min'],
            'icon21': rforecast['list'][21]['weather'][0]['icon'],



            
            'DateTime22' : rforecast['list'][22]['dt_txt'],
            'temperature22' : rforecast['list'][22]['main']['temp'],
            'feel_temp22'   : rforecast['list'][22]['main']['feels_like'],
            'max_temp22'   : rforecast['list'][22]['main']['temp_max'],
            'min_temp22'   : rforecast['list'][22]['main']['temp_min'],
            'icon22': rforecast['list'][22]['weather'][0]['icon'],


            
            'DateTime23' : rforecast['list'][23]['dt_txt'],
            'temperature23' : rforecast['list'][23]['main']['temp'],
            'feel_temp23'   : rforecast['list'][23]['main']['feels_like'],
            'max_temp23'   : rforecast['list'][23]['main']['temp_max'],
            'min_temp23'   : rforecast['list'][23]['main']['temp_min'],
            'icon23': rforecast['list'][23]['weather'][0]['icon'],



            
            'DateTime24' : rforecast['list'][24]['dt_txt'],
            'temperature24' : rforecast['list'][24]['main']['temp'],
            'feel_temp24'   : rforecast['list'][24]['main']['feels_like'],
            'max_temp24'   : rforecast['list'][24]['main']['temp_max'],
            'min_temp24'   : rforecast['list'][24]['main']['temp_min'],
            'icon24': rforecast['list'][24]['weather'][0]['icon'],



            
            'DateTime25' : rforecast['list'][25]['dt_txt'],
            'temperature25' : rforecast['list'][25]['main']['temp'],
            'feel_temp25'   : rforecast['list'][25]['main']['feels_like'],
            'max_temp25'   : rforecast['list'][25]['main']['temp_max'],
            'min_temp25'   : rforecast['list'][25]['main']['temp_min'],
            'icon25': rforecast['list'][25]['weather'][0]['icon'],



            
            'DateTime26' : rforecast['list'][26]['dt_txt'],
            'temperature26' : rforecast['list'][26]['main']['temp'],
            'feel_temp26'   : rforecast['list'][26]['main']['feels_like'],
            'max_temp26'   : rforecast['list'][26]['main']['temp_max'],
            'min_temp26'   : rforecast['list'][26]['main']['temp_min'],
            'icon26': rforecast['list'][26]['weather'][0]['icon'],



            
            'DateTime27' : rforecast['list'][27]['dt_txt'],
            'temperature27' : rforecast['list'][27]['main']['temp'],
            'feel_temp27'   : rforecast['list'][27]['main']['feels_like'],
            'max_temp27'   : rforecast['list'][27]['main']['temp_max'],
            'min_temp27'   : rforecast['list'][27]['main']['temp_min'],
            'icon27': rforecast['list'][27]['weather'][0]['icon'],



            
            'DateTime28' : rforecast['list'][28]['dt_txt'],
            'temperature28' : rforecast['list'][28]['main']['temp'],
            'feel_temp28'   : rforecast['list'][28]['main']['feels_like'],
            'max_temp28'   : rforecast['list'][28]['main']['temp_max'],
            'min_temp28'   : rforecast['list'][28]['main']['temp_min'],
            'icon28': rforecast['list'][28]['weather'][0]['icon'],

            
            'DateTime29' : rforecast['list'][29]['dt_txt'],
            'temperature29' : rforecast['list'][29]['main']['temp'],
            'feel_temp29'   : rforecast['list'][29]['main']['feels_like'],
            'max_temp29'   : rforecast['list'][29]['main']['temp_max'],
            'min_temp29'   : rforecast['list'][29]['main']['temp_min'],
            'icon29': rforecast['list'][29]['weather'][0]['icon'],

            
            'DateTime30' : rforecast['list'][30]['dt_txt'],
            'temperature30' : rforecast['list'][30]['main']['temp'],
            'feel_temp30'   : rforecast['list'][30]['main']['feels_like'],
            'max_temp30'   : rforecast['list'][30]['main']['temp_max'],
            'min_temp30'   : rforecast['list'][30]['main']['temp_min'],
            'icon30': rforecast['list'][30]['weather'][0]['icon'],

            
            'DateTime31' : rforecast['list'][31]['dt_txt'],
            'temperature31' : rforecast['list'][31]['main']['temp'],
            'feel_temp31'   : rforecast['list'][31]['main']['feels_like'],
            'max_temp31'   : rforecast['list'][31]['main']['temp_max'],
            'min_temp31'   : rforecast['list'][31]['main']['temp_min'],
            'icon31': rforecast['list'][31]['weather'][0]['icon'],

            
            'DateTime32' : rforecast['list'][32]['dt_txt'],
            'temperature32' : rforecast['list'][32]['main']['temp'],
            'feel_temp32'   : rforecast['list'][32]['main']['feels_like'],
            'max_temp32'   : rforecast['list'][32]['main']['temp_max'],
            'min_temp32'   : rforecast['list'][32]['main']['temp_min'],
            'icon32': rforecast['list'][32]['weather'][0]['icon'],

            
            'DateTime33' : rforecast['list'][33]['dt_txt'],
            'temperature33' : rforecast['list'][33]['main']['temp'],
            'feel_temp33'   : rforecast['list'][33]['main']['feels_like'],
            'max_temp33'   : rforecast['list'][33]['main']['temp_max'],
            'min_temp33'   : rforecast['list'][33]['main']['temp_min'],
            'icon33': rforecast['list'][33]['weather'][0]['icon'],

            
            'DateTime34' : rforecast['list'][34]['dt_txt'],
            'temperature34' : rforecast['list'][34]['main']['temp'],
            'feel_temp34'   : rforecast['list'][34]['main']['feels_like'],
            'max_temp34'   : rforecast['list'][34]['main']['temp_max'],
            'min_temp34'   : rforecast['list'][34]['main']['temp_min'],
            'icon34': rforecast['list'][34]['weather'][0]['icon'],


            
            'DateTime35' : rforecast['list'][35]['dt_txt'],
            'temperature35' : rforecast['list'][35]['main']['temp'],
            'feel_temp35'   : rforecast['list'][35]['main']['feels_like'],
            'max_temp35'   : rforecast['list'][35]['main']['temp_max'],
            'min_temp35'   : rforecast['list'][35]['main']['temp_min'],
            'icon35': rforecast['list'][35]['weather'][0]['icon'],


            
            'DateTime36' : rforecast['list'][36]['dt_txt'],
            'temperature36' : rforecast['list'][36]['main']['temp'],
            'feel_temp36'   : rforecast['list'][36]['main']['feels_like'],
            'max_temp36'   : rforecast['list'][36]['main']['temp_max'],
            'min_temp36'   : rforecast['list'][36]['main']['temp_min'],
            'icon36': rforecast['list'][36]['weather'][0]['icon'],

            
            'DateTime37' : rforecast['list'][37]['dt_txt'],
            'temperature37' : rforecast['list'][37]['main']['temp'],
            'feel_temp37'   : rforecast['list'][37]['main']['feels_like'],
            'max_temp37'   : rforecast['list'][37]['main']['temp_max'],
            'min_temp37'   : rforecast['list'][37]['main']['temp_min'],
            'icon37': rforecast['list'][37]['weather'][0]['icon'],

            
            'DateTime38' : rforecast['list'][38]['dt_txt'],
            'temperature38' : rforecast['list'][38]['main']['temp'],
            'feel_temp38'   : rforecast['list'][38]['main']['feels_like'],
            'max_temp38'   : rforecast['list'][38]['main']['temp_max'],
            'min_temp38'   : rforecast['list'][38]['main']['temp_min'],
            'icon38': rforecast['list'][38]['weather'][0]['icon'],

            
        }
   #return render_template("result.html",)
   print(rforecast['list'][38]['dt_txt'])
   return render_template("show.html",weatherforecast=weatherforecast)


  

if __name__ == '__main__':
    app.run(debug=True)