from flask import jsonify

class Home:
    def index(self):
        print('index() home.py')

        return jsonify({"message":"Welcome to retispec. Server is running...","status":"success","status_code":200})