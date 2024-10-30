from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

 @app.route('/runners')
def runners():
    return render_template('runners.html')

 @app.route('/update_runner/<runner_id>')
def update_runner(runner_id):
     # Fetch the runner data based on the runner_id
    return render_template('update_runner.html', runner=runner_data)