from flask import Flask, render_template, request, redirect
from datafinder import DataFinder


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('google.html')


@app.route("/summoner/")
def userData():
    user = request.args.get('userName', default="chul0te")
    region = request.args.get('region', default="la2")
    info = DataFinder(region, user)
    req = info.player_data()
    if not req:
        return render_template("nodatafound.html")

    stats = []
    for match in req:
        stats.append(info.match_stats(match))
    return render_template("summoner.html", userName=user, matchData=stats)

