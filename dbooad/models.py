from sqlalchemy import Column, Numeric, String
from config import engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base(engine)
Base.query = session.query_property()


class Customer(Base):
    """"""
    __tablename__ = 'CUSTOMER'

    IDCUSTOMER = Column(Numeric, primary_key=True)
    FIRSTNAME = Column(String(15))
    LASTNAME = Column(String(15))
    EMAIL = Column(String(15), unique=True)
    PWDHASH = Column(String(54))

    def __init__(self,IDCUSTOMER=None, FIRSTNAME=None, LASTNAME=None, EMAIL=None, password=None):
        """"""
        self.IDCUSTOMER = IDCUSTOMER
        self.FIRSTNAME = FIRSTNAME
        self.LASTNAME = LASTNAME
        self.EMAIL = EMAIL
        self.set_password(password)

    def set_password(self, password):
        self.PWDHASH = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.PWDHASH, password)


Base.metadata.create_all(bind=engine)
