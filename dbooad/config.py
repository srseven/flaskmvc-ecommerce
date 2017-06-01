from sqlalchemy import create_engine
engine = create_engine('oracle://DBPROJECT:srseven71@127.0.0.1:1521/XE', echo=True) #Network parameters for database connection
connection = engine.connect() #connect to database
result = connection.execute() #execute SQL queries here

