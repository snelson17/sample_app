from flask import Flask, render_template
from googlefinance import getQuotes

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('sample_page.html')



@app.route("/about")
def about():
	return render_template('about.html')


def get_stock_price(ticker):
	quotes = getQuotes(ticker)
	price= quotes[0]['LastTradePrice']
	return'the price of {} is {}'.format(ticker, price)


@app.route("/results")
def results():
	stock = request.values.get('stock')
	price = get_stock_price(stock)
	return render_template('results.html')

app.run(debug=True)


