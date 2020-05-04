from flask import Flask, render_template, request
from using_dictionary import get_meaning, get_synonym, get_antonym


app=Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
	input = request.form["word"]
	if input != None:
	    if request.form['submit button'] == 'Find the definition':
		result = get_meaning(input)
	    	return '''
			<html>
		    	   <body>
				<p>{result}</p>
				<p><a href="/">Click here to go on</a>
		    	   </body>
			</html>
       	   	      '''.format(result=result)
	    elif request.form['submit button'] == 'Find the synonym':
		result = get_synonym(input)
                return '''
                        <html>
                           <body>
                                <p>{result}</p>
                                <p><a href="/">Click here to go on</a>
                           </body>
                        </html>
                      '''.format(result=result)
	    elif request.form['submit button'] == 'Find the antonym':
		result = get_antonym(input)
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
