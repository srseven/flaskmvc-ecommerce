from sqlalchemy import create_engine
engine = create_engine('oracle://k142214:srseven71@127.0.0.1:1521/XE', echo=True) #Network parameters for database connection
connection = engine.connect()
result = connection.execute() #execute SQL queries here

