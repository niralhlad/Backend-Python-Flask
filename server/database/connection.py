def createDBUrl(configObj):
    dbConfig = configObj.getDBConfig()

    if dbConfig['dbPort'] is not None:
        dbURL = 'postgresql://' + dbConfig['dbUser'] + ':' + dbConfig['dbPassword'] + '@' + dbConfig['dbHost'] + '/' + dbConfig['dbName']
    else:
        dbURL = 'postgresql://' + dbConfig['dbUser'] + ':' + dbConfig['dbPassword'] + '@' + dbConfig['dbHost'] + ':' + dbConfig['dbPort'] + '/' + dbConfig['dbName']
    return dbURL