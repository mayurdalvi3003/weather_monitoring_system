from flask import Flask ,render_template ,request # this request is use for the get data from the form 
import requests # this requests is basically use for the get data from the url 

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/weather_app" ,methods = ['POST' ,"GET"])
def get_WeatherData():
    url = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {"q":request.form.get("city"),# city is a id of that particular data
                  "appid":request.form.get("appid"),
                  "units":request.form.get("units")
                  }
    
    response = requests.get(url,params= parameters)
    data = response.json()
    return f"data : {data}" # here i want my json file data as my output
if __name__ =="__main__":
    app.run(host = "0.0.0.0" )