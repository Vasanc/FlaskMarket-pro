from flask import *

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route('/market')
def market():
    items = [
        {'id':1, 'name':'Phone', 'barcode':'123', 'price':100},
        {'id':2, 'name':'Laptop', 'barcode':'246', 'price':200},
        {'id':3, 'name':'Keyboard', 'barcode':'369', 'price':300}
    ]
    return render_template('market.html', items = items)


if __name__=='__main__':
    app.run(port=4000, debug=True)
    print('hello world')
    
    