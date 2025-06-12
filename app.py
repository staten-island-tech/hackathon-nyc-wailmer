from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://data.cityofnewyork.us/resource/8pnn-kkif.json")
    data = response.json()
    college_list = data['results']

    colleges = []

    for college in college_list:
        colleges.append({
            'name': college['name'],
            'url': college['url'],
            'streetname': college['streetname']
        })