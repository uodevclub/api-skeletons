from urllib2 import Request, urlopen
from urllib import quote_plus
from flask import Flask, request, render_template
import json

app = Flask(__name__)

# HTTP Headers used for API
headers = {
  'Content-Type': 'application/json', 					# Content-Type, tell the request you want JSON
  'trakt-api-version': '2',								# API Version
  'trakt-api-key': '<your-api-key>'						# API Key
}

@app.route("/", methods=['GET', 'POST'])
def index():
	'''
		Search Trakt.TV
	'''

	if request.method == "POST":
		q = quote_plus(request.form.get("query"))
		if len(q) == 0:
			return render_template('index.html')
		r = Request('https://api-v2launch.trakt.tv/search?query='+q, headers=headers)
		response_body = urlopen(r).read()
		return render_template('index.html', result=response_body)

	return render_template('index.html')

@app.route("/trending")
def trending():
	'''
		Get a list of trending TV Shows
	'''

	r = Request('https://api-v2launch.trakt.tv/shows/trending', headers=headers)
	response_body = urlopen(r).read()
	return response_body

if __name__ == "__main__":
    app.run(debug=True)