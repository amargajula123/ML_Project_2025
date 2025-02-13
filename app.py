from flask import Flask
import sklearn

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():
    return "Starting Machine Learning MODELS And Practice"

if __name__=="__main__":
    app.run(debug=True)