import os
import requests
@app.route('/api/v1/albums')
def album_json():
   return jsonify(json_info)

@app.route('/api/v1/movies/search_title', methods=['GET'])
def search_title():
    results = []
    if 'title' in requests.args:
        title = request.args['title']

        for movie in movie['title']:
            results.append(movie)
