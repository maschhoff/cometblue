# Mathias Aschhoff 2018 - 
# REQUIRED pip3 install flask
# !! RUNNING ON python3 because of timeout parameter

#!flask/bin/python
from flask import Flask
from subprocess import check_output
import shlex
import logging
import openweathermap

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Heizungsserver up and running!</h1>"

@app.route('/<string:MAC>/<string:TEMP>', methods=['GET'])
def set_cometblue(MAC,TEMP):
    try:
        cmd="cometblue -a hci0 device -p 0000 "+MAC+" set temperatures -m "+TEMP
        args=shlex.split(cmd)
        process=check_output(args) 
        #out=process.decode("utf-8")
        logging.info("OK - TEMPERATUR VON "+MAC+" AUF "+TEMP+" GRAD")
        return str("OK - TEMPERATUR VON "+MAC+" AUF "+TEMP+" GRAD")
    except:
        print("ERROR!")
        return "Es ist ein Fehler aufgetreten!"

@app.route('/weather/', methods=['GET'])
def get_weather():
	openweathermap.init()
	logging.info("OpenWeatherMap wurden an openHAB uebertragen")
	return "OpenWeatherMap wurden an openHAB uebertragen"

if __name__ == '__main__':
	logging.basicConfig(filename='server.log',level=logging.DEBUG)
	logging.info("Starte Heizungsserver...")
	app.run(host='0.0.0.0',port=3247,debug=True)
