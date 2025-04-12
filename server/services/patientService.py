from flask import jsonify
from database.models.patientModel import PatientModel
from database.dbConn import db
import json

class PatientService:
    def createPatient(self,requestBody):
        
        if PatientModel.query.filter_by(patient_id=requestBody['patient_id']).first() is not None:
            return "duplicate"

        patientObj = PatientModel(
            patient_id = requestBody['patient_id'],
            first_name = requestBody['first_name'].lower(), 
            last_name = requestBody['last_name'].lower(), 
            birth_date= requestBody['birth_date'], 
            sex = requestBody['sex'].lower()
        )

        db.session.add(patientObj)
        db.session.commit()

        return "success"
    
    def getPatientbyID(self,patientID): 
        patient = PatientModel.query.filter_by(patient_id=patientID).first()
        if patient is not None:
            return {
                "patient_id": patient.patient_id,
                "first_name": patient.first_name,
                "last_name": patient.last_name,
                "birth_date": patient.birth_date,
                "sex": patient.sex
            }
        return None
    
    def deletePatientbyID(self,patientID):
        patient = PatientModel.query.filter_by(patient_id=patientID)
        if patient is not None:
            patient.delete()
            db.session.commit()
            return True
        return None
    
    def getPatient(self,firstName,lastName):
        patients = PatientModel.query.filter_by(first_name=firstName,last_name=lastName)
        data = []
        for patient in patients:
            temp = {
                "patient_id": patient.patient_id,
                "first_name": patient.first_name,
                "last_name": patient.last_name,
                "birth_date": patient.birth_date,
                "sex": patient.sex
            }
            data.append(temp)
        print(data)
        return data