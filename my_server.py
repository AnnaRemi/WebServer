from flask import Flask, render_template, request
import json
from PyDictionary import PyDictionary


app=Flask(__name__)
app.config["DEBUG"] = True

d=PyDictionary()

@app.route('/api/meaning/<name>',methods=['GET'])
def meaning(name):
        value=d.meaning(name)
        if value is None:
                return json.dumps({'error':'Word has no meaning in API'})
        return json.dumps(value)


@app.route('/api/synonym/<name>',methods=['GET'])
def synonym(name):
        value=d.synonym(name)
        if value is None:
                return json.dumps({'error':'Word has no synonym in API'})
        return json.dumps(value)


@app.route('/api/antonym/<name>',methods=['GET'])
def antonym(name):
        value=d.antonym(name)
        if value is None:
                return json.dumps({'error':'Word has no antonym in API'})
        return json.dumps(value)


@app.route('/api/translate/<lang>/<word>',methods=['GET'])
def translate(lang,word):
        return d.translate(word,lang)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
	input = request.form["word"]
	if input != None:
            result = meaning(input)
	    return '''
		<html>
		    <body>
			<p>{result}</p>
			<p><a href="/">Click here to go on</a>
		    </body>
		</html>
       	   '''.format(result=result)

    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
