from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models import Base, Department, Employee

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

def init_db():
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)

    engineering = Department(name='Engineering')
    db_session.add(engineering)

    hr = Department(name='Human Resources')
    db_session.add(hr)

    db_session.add(Employee(name='Peter', department=engineering))
    db_session.add(Employee(name='Roy', department=engineering))
    db_session.add(Employee(name='Tracy', department=hr))

    db_session.commit()
