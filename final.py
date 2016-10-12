from flask import Flask, render_template, request
import giphypop
from googlefinance import getQuotes

# g = giphypop.Giphy()
# results = g.search('cats') # returns a list of objects
# for result in results:
# 	print(result.media_url)
# 	print(result.url)

#http://media0.giphy.com/media/26uf9IAZN7JvvYbwA/giphy.gif # Media (image) Url
#http://giphy.com/gifs/love-cat-cats-26uf9IAZN7JvvYbwA # GIF Url
#http://media1.giphy.com/media/26uf5hiFbD0DdZdGo/giphy.gif
#http://giphy.com/gifs/cat-judgemental-judgey-26uf5hiFbD0DdZdGo

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('final_index.html')

@app.route("/about")
def about():
	return render_template('finalabout.html')

@app.route("/results")
def results():
	search_term = request.values.get('searchterm')
	g = giphypop.Giphy()
	results = g.search(search_term)
	# for result in results:
	# 	media_url.append(result.media_url)
	# 	url.append(result.url)
	return render_template('finalresults.html',searchterm = search_term, results=results)

app.run(debug=True)