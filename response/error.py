class ErrorResponse:
    JSON_BODY_ERROR = {
        "error":"JSON Body Missing",
        "message":"BAD REQUEST"
    }

    INVALID_URL_ERROR = {
        "error":"Invalid Request",
        "message":"INVALID REQUEST",
        "custom_code":"NO_URL_FOUND"
    }

    NO_PATIENT_ERROR = {
        "error":"Invalid Patient ID",
        "message":"No patient found with patient_id : ",
        "custom_code":"NO_PATIENT_FOUND"
    }

    DUPLICATE_PATIENT_ID = { 
        "error":"Duplicate Resource", 
        "message":"patient_id already exists",
        "custom_code":"DUPLICATE_PATIENT_ID"
    }

    INVALID_BODY = { 
        "error":"Bad Request", 
        "message":"Please check your request body",
        "custom_code":"INVALID_REQUEST_BODY"
    }


