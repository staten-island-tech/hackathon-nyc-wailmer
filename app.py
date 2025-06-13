from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://data.cityofnewyork.us/resource/8pnn-kkif.json")
    college_list = response.json()

    colleges = []

    for college in college_list:
        colleges.append({
            'name': college['name'],
            'url': college['url'],
            'streetname': college['streetname']
        })
    return render_template("index.html", colleges=colleges)

if __name__ == '__main__':
    app.run(debug=True)