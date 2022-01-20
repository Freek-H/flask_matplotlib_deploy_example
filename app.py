from flask import Flask, render_template

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
    return render_template('plot_jinja.html', img_path='static/plot.png')
