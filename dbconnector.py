from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import event

_engine = None

Session = sessionmaker()

def connect_to_inmemory_db():
    global _engine
    _engine = create_engine('sqlite:///:memory:', echo=True)
    event.Base.metadata.create_all(_engine)
    Session.configure(bind=_engine)

def connect_to_db(dblocation):
    global _engine
    _engine = create_engine(dblocation, echo=True)
    Session.configure(bind=_engine)
