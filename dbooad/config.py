# from dbooad import app
from sqlalchemy import create_engine


engine = create_engine('oracle://k142214:srseven@127.0.0.1:1521/XE', echo=True)
