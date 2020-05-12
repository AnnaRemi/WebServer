from flask import Flask, render_template, request
from PyDictionary_library import get_meaning, get_translation

app=Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def get_home():
    if request.method == "POST":
	input = request.form["word"]
	MESSAGE = '''
    		<html>
		    <body>
			<p>{result}</p>
			<p><a href="/">Click here to go on</a>
	    	    </body>
		</html>
               '''
	if input != None:
	    if request.form["submit_button"] == "Find the definition": 
	        result = get_meaning(input)
	        return MESSAGE.format(result=result)

	    elif request.form["submit_button"] == "Find the translation":
		code = request.form["code"]
		result = get_translation(code, input)
		return MESSAGE.format(result=result)

    return render_template("home.html")


@app.route("/about")
def get_about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
