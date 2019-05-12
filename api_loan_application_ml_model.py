import datetime
import logging
import os

from flask import Flask, request
from flask_cors import CORS

from service_api_default_predict_model.decisiontree_1 import predict_default

application = Flask(__name__)


@application.route('/', methods=['GET'])
def hello():
    return "hello"


@application.route('/loan_decision_ml_model/v1/business_id/<business_id>', methods=['GET'])
def loan_decision_ml_model(business_id):
    return predict_default(business_id)

CORS(application)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
