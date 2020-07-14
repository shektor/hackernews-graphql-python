from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship


Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    department_id = Column(Integer, primary_key=True)
    name = Column(String)

class Role(Base):
    __tablename__ = 'roles'
    role_id = Column(Integer, primary_key=True)
    name = Column(String)

class Employee(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    name = Column(String)
    deparment_id = Column(Integer, ForeignKey('departments.department_id'))
    role_id = Column(Integer, ForeignKey('roles.role_id'))
    department = relationship(
        Department, 
        backref=backref('employees', uselist=True, cascade='delete,all')
    )
    role = relationship(
        Role, 
        backref=backref('roles', uselist=True, cascade='delete,all')
    )
