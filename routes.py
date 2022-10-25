from urllib import request
from flask import current_app as app
from flask import request, jsonify
import copy

from services.home import Home
from services.patientService import PatientService
from response.error import ErrorResponse
from response.success import SuccessResponse
from util import helper

customError = ErrorResponse()
customSuccess = SuccessResponse()

@app.route('/')
def index():
    return Home().index()

@app.route('/patient/create', methods=['POST'])
def createPatient():
    print("---- /patient/create ----")
    
    if not request.is_json:
        print("Response: ", customError.JSON_BODY_ERROR)
        return jsonify(customError.JSON_BODY_ERROR), 400
    
    requestBody =  request.get_json()
    print(requestBody)

    if not helper.validateRequestBody('createPatient',requestBody):
        return customError.INVALID_BODY, 400
    
    responseData = PatientService().createPatient(requestBody)
    
    if responseData == "duplicate":
        return customError.DUPLICATE_PATIENT_ID
    
    return customSuccess.PATIENT_CREATED, 200

@app.route('/patient/search/id/<patientID>', methods=['GET'])
def getPatientbyID(patientID):
    print("---- /patient/search/id ----")
    data = PatientService().getPatientbyID(patientID)
    if data is None:
        responseData = copy.deepcopy(customError.NO_PATIENT_ERROR)
        responseData['message'] += patientID
        return jsonify(responseData), 404

    responseData = copy.deepcopy(customSuccess.PATIENT_FETCHED)
    responseData['data'].append(data)
    print(responseData)
    return jsonify(responseData), 200 

@app.route('/patient/delete', methods=['DELETE'])
def deletePatient():
    print("---- patient/delete ----")

    if not request.is_json:
        print("Response: ", customError.JSON_BODY_ERROR)
        return jsonify(customError.JSON_BODY_ERROR), 400

    requestBody =  request.get_json()
    print(requestBody)

    if not helper.validateRequestBody('deletePatient',requestBody):
        return customError.INVALID_BODY, 400

    patientID = str(requestBody['patient_id']).lower()

    data = PatientService().deletePatientbyID(patientID)
    print(data)
    if data is None:
        responseData = copy.deepcopy(customError.NO_PATIENT_ERROR)
        responseData['message'] += patientID
        return jsonify(responseData), 404

    return jsonify(customSuccess.PATIENT_DELETED), 200 


@app.route('/patient/search', methods=['POST'])
def getPatient():
    print("---- /patient/search ----")
    
    if not request.is_json:
        print("Response: ", customError.JSON_BODY_ERROR)
        return jsonify(customError.JSON_BODY_ERROR), 400
    
    requestBody =  request.get_json()
    print(requestBody)

    if not helper.validateRequestBody('searchPatient',requestBody):
        return customError.INVALID_BODY, 400
    
    firstName = requestBody['first_name']
    lastName = requestBody['last_name']

    data = PatientService().getPatient(firstName,lastName)
    
    if data is None:
        responseData = copy.deepcopy(customError.NO_PATIENT_ERROR)
        responseData['message'] +=  firstName + ' ' + lastName
        return jsonify(responseData), 404
    
    responseData = copy.deepcopy(customSuccess.PATIENT_FETCHED)
    responseData['data'] = data
    print(responseData)
    return jsonify(responseData), 200

@app.route('/<path:path>')
def catch_all(path):
    return jsonify(customError.INVALID_URL_ERROR), 400