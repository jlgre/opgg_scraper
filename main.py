from flask import Flask, jsonify, render_template

import tier_list
import skill_order
import build

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tierlist/<lane>', methods=['GET'])
def api_tier_list(lane):
    places, names, win_rates, ban_rates = tier_list.get(lane)
    objects = []
    for i in range(len(places)):
        objects.append({
            'place': places[i],
            'name': names[i],
            'win_rate': win_rates[i],
            'ban_rate': ban_rates[i]
        })
    return jsonify(
        objects
    )


@app.route('/build/<lane>/<champ>')
def api_build(lane, champ):
    raw = build.get(lane, champ)
    obj = {}
    for entry in raw:
        obj[entry[0]] = entry[1]
    return jsonify(obj)


@app.route('/skillorder/<lane>/<champ>')
def api_skill_order(lane, champ):
    return jsonify(skill_order.get(lane, champ))


if __name__ == '__main__':
    app.run(port=8888)
