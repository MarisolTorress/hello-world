from flask import Flask, render_template, request, json, jsonify
import os
import requests

app = Flask(_name_, static folder="static")

movies_data = os.path.join(app.static_folder, 'data', 'movies.json')

@app.route('/api/v1/movies/all', methods=['GET'])
def api_movies_all():
    with open(movies_data, 'r') as jsondata:
        movies = json.load(jsondata)
   return jsonify(movies)

@app.route('/')
def index():
    return render_template('index.html')
    app.run(debug=True, host='0.0.0.0')