from flask import *

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route('/market')
def market():
    return render_template('market.html')
if __name__=='__main__':
    app.run(port=4000, debug=True)
    
    