from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HosingException


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():
    try:
        raise Exception("we are testing Custome Exception")
    except Exception as e:
        housing=HosingException(e,sys)
        logging.info(housing.error_massage)
        logging.info("we are testing logging module")
    return "Starting Machine Learning MODELS And Practice"

if __name__=="__main__":
    app.run(debug=True)