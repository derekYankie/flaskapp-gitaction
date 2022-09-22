# Assignment: CI / CD: Flask webapp with Docker & GitHub Actions
# https://flask.palletsprojects.com/en/1.1.x/quickstart/
# Flask==0.12 (https://flask.palletsprojects.com/en/0.12.x/upgrading/#version-0-12)
# Date: 09/21/2022
# "Hey Siri, play September by Earth, Wind & Fire"
# Author: derekYankie
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, From Flask via Github Action!!!'
    
