from flask import Flask, request
import json
import requests
from PyDictionary import PyDictionary
from translate import Translator
import pprint 
from pprint import pformat


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/meaning/<name>', methods=['GET'])
def get_meaning(name):
    dictionary = PyDictionary()
    value = dictionary.meaning(name)
    if value is None:
        return json.dumps({'error': 'Word has no meaning in API'})
    return value


@app.route('/api/translate/<code>/<word>', methods=['GET'])
def get_translation(word, code):
    lang = str(code)
    translator = Translator(to_lang = lang)
    value = translator.translate(str(word))
    if value is None:
        return json.dumps({'error': 'Word has no translation in API'})
    return json.dumps(value, ensure_ascii=False).encode('utf8')

