# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 11, 2024 20:04:40
# Database: sqlite:////tmp/tmp.T0mOrgtWuP/Boat_yard/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Table to store information about customers.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    address = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    BoatList : Mapped[List["Boat"]] = relationship(back_populates="customer")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="customer")



class Employee(SAFRSBaseX, Base):
    """
    description: Table for employees working at the boat yard.
    """
    __tablename__ = 'employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    hire_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    MaintenanceList : Mapped[List["Maintenance"]] = relationship(back_populates="employee")



class Part(SAFRSBaseX, Base):
    """
    description: Table for details about parts and upgrades.
    """
    __tablename__ = 'part'
    _s_collection_name = 'Part'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="part")



class Service(SAFRSBaseX, Base):
    """
    description: Table to list types of services offered.
    """
    __tablename__ = 'service'
    _s_collection_name = 'Service'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="service")



class Boat(SAFRSBaseX, Base):
    """
    description: Table to store information about boats owned by customers.
    """
    __tablename__ = 'boat'
    _s_collection_name = 'Boat'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    length = Column(Float)
    customer_id = Column(ForeignKey('customer.id'))

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("BoatList"))

    # child relationships (access children)
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="boat")
    CleaningList : Mapped[List["Cleaning"]] = relationship(back_populates="boat")
    MaintenanceList : Mapped[List["Maintenance"]] = relationship(back_populates="boat")
    RepairList : Mapped[List["Repair"]] = relationship(back_populates="boat")
    StorageList : Mapped[List["Storage"]] = relationship(back_populates="boat")



class Order(SAFRSBaseX, Base):
    """
    description: Table for parts orders by customers.
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    part_id = Column(ForeignKey('part.id'))
    order_date = Column(DateTime)
    quantity = Column(Integer, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))
    part : Mapped["Part"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)



class Appointment(SAFRSBaseX, Base):
    """
    description: Table to schedule services for boats.
    """
    __tablename__ = 'appointment'
    _s_collection_name = 'Appointment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    boat_id = Column(ForeignKey('boat.id'))
    service_id = Column(ForeignKey('service.id'))
    appointment_datetime = Column(DateTime)
    notes = Column(String)

    # parent relationships (access parent)
    boat : Mapped["Boat"] = relationship(back_populates=("AppointmentList"))
    customer : Mapped["Customer"] = relationship(back_populates=("AppointmentList"))
    service : Mapped["Service"] = relationship(back_populates=("AppointmentList"))

    # child relationships (access children)
    BillingList : Mapped[List["Billing"]] = relationship(back_populates="appointment")



class Cleaning(SAFRSBaseX, Base):
    """
    description: Table for cleaning service records.
    """
    __tablename__ = 'cleaning'
    _s_collection_name = 'Cleaning'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    boat_id = Column(ForeignKey('boat.id'))
    cleaning_date = Column(DateTime)
    cost = Column(Float, nullable=False)

    # parent relationships (access parent)
    boat : Mapped["Boat"] = relationship(back_populates=("CleaningList"))

    # child relationships (access children)



class Maintenance(SAFRSBaseX, Base):
    """
    description: Table for scheduled maintenance tasks for boats.
    """
    __tablename__ = 'maintenance'
    _s_collection_name = 'Maintenance'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    boat_id = Column(ForeignKey('boat.id'))
    employee_id = Column(ForeignKey('employee.id'))
    maintenance_date = Column(DateTime)
    details = Column(String)

    # parent relationships (access parent)
    boat : Mapped["Boat"] = relationship(back_populates=("MaintenanceList"))
    employee : Mapped["Employee"] = relationship(back_populates=("MaintenanceList"))

    # child relationships (access children)



class Repair(SAFRSBaseX, Base):
    """
    description: Table for engine repair services records.
    """
    __tablename__ = 'repair'
    _s_collection_name = 'Repair'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    boat_id = Column(ForeignKey('boat.id'))
    description = Column(String)
    repair_date = Column(DateTime)
    cost = Column(Float, nullable=False)

    # parent relationships (access parent)
    boat : Mapped["Boat"] = relationship(back_populates=("RepairList"))

    # child relationships (access children)



class Storage(SAFRSBaseX, Base):
    """
    description: Table for boats storing details.
    """
    __tablename__ = 'storage'
    _s_collection_name = 'Storage'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    boat_id = Column(ForeignKey('boat.id'))
    location = Column(String, nullable=False)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    # parent relationships (access parent)
    boat : Mapped["Boat"] = relationship(back_populates=("StorageList"))

    # child relationships (access children)



class Billing(SAFRSBaseX, Base):
    """
    description: Table for billing and payment records for services.
    """
    __tablename__ = 'billing'
    _s_collection_name = 'Billing'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    appointment_id = Column(ForeignKey('appointment.id'))
    total_amount = Column(Float, nullable=False)
    payment_date = Column(DateTime)
    status = Column(String, nullable=False)

    # parent relationships (access parent)
    appointment : Mapped["Appointment"] = relationship(back_populates=("BillingList"))

    # child relationships (access children)
