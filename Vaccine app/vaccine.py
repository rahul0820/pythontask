import flask
from flask.templating import render_template
app = flask.Flask(__name__)

app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    print("checking if fuction is working")    
    return "Please hit approprite end point /login or /Register"

@app.route('/login', methods=['GET'])
def login():
    print("login is working")
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register():
    print("register is working")
    return render_template('register.html')

@app.route('/home', methods=['GET'])
def homepage():
    print("home is working")
    return render_template('home.html')

@app.route('/Thankyou', methods=['GET'])
def thankyou():
    print("thank you page is working")
    return render_template('Thankyou.html')

app.run(host='0.0.0.0', port=3000)