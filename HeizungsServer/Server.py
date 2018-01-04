# Mathias Aschhoff 2018 - 
# REQUIRED pip3 install flask
# !! RUNNING ON python3 because of timeout parameter

#!flask/bin/python
from flask import Flask
from subprocess import check_output
import shlex

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Heizungsserver up and running!</h1>"

@app.route('/<string:MAC>/<string:TEMP>', methods=['GET'])
def get_test(MAC,TEMP):
    try:
        cmd="cometblue device -p 0 "+MAC+" set temperatures -m "+TEMP
        args=shlex.split(cmd)
        process=check_output(args) 
        #out=process.decode("utf-8")
        return str("OK - TEMPERATUR VON "+MAC+" AUF "+TEMP+" GRAD")
    except:
        print("ERROR!")
        return "Es ist ein Fehler aufgetreten!"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3247,debug=True)
