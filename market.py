from flask import *
from flask_sqlalchemy import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length = 30), nullable = False, unique = True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length = 12), nullable = False, unique=True)
    description = db.Column(db.String(length = 1024), nullable = False, unique = True)
    
    def __repr__(self):
        return f'Item {self.name}'
    
    

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/market')
def market():
    items = Item.query.all()
    return render_template('market.html', items = items)


if __name__=='__main__':
    app.run(port=4000, debug=True)
    
    
    