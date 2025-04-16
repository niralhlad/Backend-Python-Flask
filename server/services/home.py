from flask import jsonify

class Home:
    def index(self):
        print('index() home.py')

        return jsonify({"message":"Welcome to Niral's Test Backend Server.","status":"success","status_code":200})
