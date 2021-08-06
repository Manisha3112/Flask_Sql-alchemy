from flask import request
import logging

from app import app
logging.basicConfig(filename='debug.log',level=logging.DEBUG)

@app.after_request
def after_request_callback(response):
    response_value=response.get_data()
    app.logger.debug(response_value.decode("utf-8"))
    return response

@app.before_request
def before_request_callback():
    app.logger.info("info login")    