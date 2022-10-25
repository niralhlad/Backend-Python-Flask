from util import helper

body = {
    "patient_id":"   h",
    "first_name":"Niral",
    "last_name":"lad",
    "birth_date":"17-01-1996",
    "sex":"male"
}
print(helper.validateRequestBody('createPatient',body))