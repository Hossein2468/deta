from flask import Flask 
app = Flask(__name__) 

@app.route('/') 
def hi() : 
    return f'Hello to you, welcome to this website' 