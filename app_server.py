from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

@app.before_request
def load_model():
    while True:
        try:
            app.model = pickle.load(open("/data/model.pkl", "rb"))
            print('model loaded')
            break
        except:
            print('model not loaded')

load_model()

@app.route("/api/recommend", methods=["POST"])
def recommend():
    mdl = app.model['model']
    version = app.model['version']
    model_date = app.model['model_date']

    # print(app.model['model'].rules)

    re_songs = request.json
    songs = pd.DataFrame(re_songs)
    songs = songs.rename({'songs': 'track_name'}, axis=1)
    
    tracklist = mdl.recommend(songs)

    res = dict(
        tracklist = tracklist,
        version = version,
        model_date = model_date
    )

    return jsonify(res)
