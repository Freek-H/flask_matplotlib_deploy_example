from datetime import datetime
from flask import Flask, render_template
import requests

from create_plot import create_plot

create_plot()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/html')
def hello_html():
    return render_template('hello.html')


@app.route('/plot')
def show_plot():
    return render_template('plot.html')


@app.route('/plot_jinja')
def show_plot_jinja():
    catfact = requests.get('https://catfact.ninja/fact').json()
    print(catfact)
    return render_template('plot_jinja.html',
                           img_path='static/plot.png',
                           timestamp=f'{datetime.now()}',
                           catfact=catfact)
