from flask import Flask, request
import json
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


@app.route('/api/synonym/<name>',methods=['GET'])
def get_synonym(name):
	dictionary=PyDictionary()
        value=dictionary.synonym(name)
        if value is None:
                return json.dumps({'error':'Word has no synonym in API'})
        return json.dumps(value)



@app.route('/api/antonym/<name>',methods=['GET'])
def get_antonym(name):
	dictionary=PyDictionary()
        value=dictionary.antonym(name)
        if value is None:
                return json.dumps({'error':'Word has no antonym in API'})
	return json.dumps(value)
