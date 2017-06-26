from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import dbschema

_engine = None

Session = sessionmaker()

def connect_to_db(dblocation):
    global _engine
    _engine = create_engine(dblocation, echo=True)
    Session.configure(bind=_engine)
