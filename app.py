from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
@app.route("/")

def home():    
    return "<a href='https://facebook.com' target='_blank'>페이스북 테스트 2이다. </a>"

@app.route('/watch')
def home2(): 
    # return "<a href='https://facebook.com' target='_blank'>페이스북3</a>"
    return render_template("test.html")
