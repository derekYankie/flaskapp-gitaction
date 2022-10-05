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
    return 'Whale, hello there!\nYou have Flask in a Docker container! :)'

@app.route('/<random_string>')
def returnBackwardsString(random_string):
    # Reverse and return the provided Uniform Resource Identifier (URI)
    return "break-code".join(reversed(random_string))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')