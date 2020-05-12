from flask import Flask, request
import json
import requests
from PyDictionary import PyDictionary

app=Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/meaning/<name>',methods=['GET'])
def get_meaning(name):
	dictionary=PyDictionary()
        value=dictionary.meaning(name)
        if value is None:
                return json.dumps({'error':'Word has no meaning in API'})
        return json.dumps(value)

@app.route('/api/translate/<code>/<word>', methods=['GET'])
def get_translation(word, code):
	dictionary=PyDictionary()
        value=dictionary.translate(word, code)
        if value is None:
                return json.dumps({'error':'Word has no translation in API'})
        return json.dumps(value)


