from util.requestBodyModel import requestBodyModel

def validateRequestBody(request,requestBody):
    validate = requestBodyModel[request]
    print(requestBody)
    for key in validate:
        if key not in requestBody:
            return False
        if requestBody[key] is None:
            return False
        if not requestBody[key] or not requestBody[key].strip():
            return False
    return True
