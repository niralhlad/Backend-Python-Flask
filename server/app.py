from flask import Flask

from server.config.config import Config
from server.database.connection import createDBUrl
from server.database.dbConn import db

configObj = Config()

def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    dbURL = createDBUrl(configObj)

    app.config["SQLALCHEMY_DATABASE_URI"] = dbURL
    
    db.init_app(app)

    with app.app_context():
        import routes

        from database.models.patientModel import PatientModel
        db.create_all()

        return app
    

if __name__ == '__main__':
    app = create_app()
    debugMode = configObj.getDebugMode()
    if(debugMode.lower() == 'false'):
        debugMode = False
    else:
        debugMode = True
    hostConfig = configObj.getHostConfig()
    app.run(debug=debugMode,port=hostConfig['port'],host=hostConfig['host'])
