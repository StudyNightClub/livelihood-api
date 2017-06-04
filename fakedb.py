from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import event

_engine = None

Session = sessionmaker()

def get_engine():
    global _engine
    if not _engine:
        _engine = create_engine('sqlite:///:memory:', echo=True)
        event.Base.metadata.create_all(_engine)
        Session.configure(bind=_engine)
    return _engine

def get_session():
    get_engine()
    return Session()
