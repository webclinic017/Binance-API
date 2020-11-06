from flask import Flask, render_template
import config, csv
from binance.client import Client
from binance.enums import *

# from jinja2 import Template

app = Flask(__name__)

client = Client(config.API_KEY, config.API_SECRET, tld='com')

@app.route('/')
def index():
    title = 'CoinView'

    info = client.get_account()

    balances = info['balances']

    return render_template('index.html', title=title, my_balances = balances)

@app.route('/buy')
def buy():
    order = client.create_order(symbol='LTC',side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=,

    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'     

@app.route('/settings')
def settings():
    return 'settings'        