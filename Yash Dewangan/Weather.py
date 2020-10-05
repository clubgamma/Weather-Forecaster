from flask import Flask, render_template, request
import os

import requests
app = Flask(__name__)



url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=<YOUR_API_KEY' #



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

"""@app.route('/show',methods=['GET', 'POST'])
def result():"""
  

if __name__ == '__main__':
    app.run(debug=True)