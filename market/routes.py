from market import app
from flask import render_template
from market.model import Item
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/market')
def market():
    items = Item.query.all()
    return render_template('market.html', items = items)