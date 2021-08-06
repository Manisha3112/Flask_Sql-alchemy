from flask_json_schema import JsonSchema
from flask import Flask, jsonify, request
from app.__init__ import app

schema = JsonSchema(app)

validation_schema = {
    'required': ['Student_Name','Student_department'],
    'properties': {
        'Student_Name': { 'type': 'string' },
        'Student_department': { 'type': 'string' },
    }
}
