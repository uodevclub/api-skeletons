from flask import Flask, render_template, request
from imdb import IMDb
app = Flask(__name__)
ia = IMDb()

@app.route("/", methods=['GET', 'POST'])
def index():
	'''
		Search for an actor on IMDb using the 'query' POST parameter

		Return a list of names
	'''

	if request.method == "POST":
		names = []
		person_search = ia.search_person(request.form.get("query"))
		for person in person_search:
			names.append(person['name'])
		return render_template('index.html', names=names)

	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)