class SuccessResponse:
    PATIENT_CREATED = {
        "status" : "success",
        "message" : "Successfully done",
        "custom_code": "PATIENT_CREATED_SUCCESSFULLY"
    }

    PATIENT_DELETED = {
        "status" : "success",
        "message" : "Successfully done",
        "custom_code": "PATIENT_DELETED_SUCCESSFULLY"
    }

    PATIENT_FETCHED = {
        "status" : "success",
        "message" : "Successfully done",
        "data": [],
        "custom_code": "PATIENT_FETCHED_SUCCESSFULLY"
    }

    SUCCESS = {
        "message" : "Successfully done",
        "status" : "success"
    }