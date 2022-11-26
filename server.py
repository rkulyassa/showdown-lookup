import flask
from flask import request, send_from_directory, jsonify
import requests
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route('/', methods=['GET'])
def home():
	with open('static/index.html') as f:
		return f.read()

@app.route('/<path:path>', methods=['GET'])
def send_static(path):
	return send_from_directory('static', path)

@app.route('/pokemon/<pokemon>', methods=['GET'])
def send_pokemon(pokemon):
	res = requests.get(f'https://www.smogon.com/dex/bw/pokemon/{pokemon}/').text
	res = res[res.find('dexSettings')+14:]
	pokemon_data = json.loads(res[:res.find('</script>')])
	return pokemon_data

app.run()