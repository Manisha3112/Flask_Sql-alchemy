from flask import Flask, request, Response, jsonify
from flask_json_schema import JsonSchema, JsonValidationError
from app.services.info.information import Student
from app import app
from app.routes.validation.validation import schema,validation_schema
from app.utils import logging


#Read all student information 
@app.route('/student_information', methods=['GET'])
def read_all_information():
    
     return jsonify({'Student_information': Student.read_all_information()})


#Read student information by id
@app.route('/student_informations', methods=['GET'])
def read_information_by_id():
    id=request.args.get('id')
    read_data = Student.read_information_by_id(id)
    return jsonify(read_data)


#Create student information 
@app.route('/student_information', methods=['POST'])
@schema.validate(validation_schema)
def create_information():
    request_data = request.get_json()  
    Student.create_information(request_data["Student_Name"], request_data["Student_department"])
    return {'status':200,'message':'Student information created'}


#Update student information 
@app.route('/student_information', methods=['PUT'])
@schema.validate(validation_schema)
def update_information():
    id=request.args.get('id')
    request_data = request.get_json()
    Student.update_information(id, request_data['Student_Name'], request_data['Student_department'])
    return {'status':200,'message':'Student information updated'}


#Delete student information 
@app.route('/student_information', methods=['DELETE'])

def delete_information():
    id=request.args.get('id')
    Student.delete_information(id)
    return {'status':200,'message':'Student information deleted'}


@app.errorhandler(JsonValidationError)

def validation_error(e):
    return jsonify({ 'error': e.message, 'errors': [validation_error.message for validation_error  in e.errors]})
