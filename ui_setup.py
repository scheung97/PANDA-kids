from flask import Flask, render_template
from redislite import Redis

app = Flask(__name__)

@app.route('/')
def selection():
    # set up selection to go to hospital, home, or education
    return render_template('base.html', title='selection')

@app.route('/<page_type>/')
def pages(page_type='hospital'):
    # page_type = hospital, home, or education
    return 'PAGES {}'.format(page_type)

@app.route('/settings/')
def settings():
    return 'SETTINGS'
