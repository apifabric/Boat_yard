import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Customer(Base):
    """
    description: Table to store information about customers.
    """
    __tablename__ = 'customer'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)

class Boat(Base):
    """
    description: Table to store information about boats owned by customers.
    """
    __tablename__ = 'boat'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    length = Column(Float, nullable=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))

class Service(Base):
    """
    description: Table to list types of services offered.
    """
    __tablename__ = 'service'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)

class Appointment(Base):
    """
    description: Table to schedule services for boats.
    """
    __tablename__ = 'appointment'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    boat_id = Column(Integer, ForeignKey('boat.id'))
    service_id = Column(Integer, ForeignKey('service.id'))
    appointment_datetime = Column(DateTime, default=datetime.datetime.utcnow)
    notes = Column(String, nullable=True)

class Storage(Base):
    """
    description: Table for boats storing details.
    """
    __tablename__ = 'storage'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    boat_id = Column(Integer, ForeignKey('boat.id'))
    location = Column(String, nullable=False)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime, nullable=True)

class Part(Base):
    """
    description: Table for details about parts and upgrades.
    """
    __tablename__ = 'part'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)

class Order(Base):
    """
    description: Table for parts orders by customers.
    """
    __tablename__ = 'order'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    part_id = Column(Integer, ForeignKey('part.id'))
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    quantity = Column(Integer, nullable=False)

class Employee(Base):
    """
    description: Table for employees working at the boat yard.
    """
    __tablename__ = 'employee'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    hire_date = Column(DateTime, default=datetime.datetime.utcnow)

class Maintenance(Base):
    """
    description: Table for scheduled maintenance tasks for boats.
    """
    __tablename__ = 'maintenance'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    boat_id = Column(Integer, ForeignKey('boat.id'))
    employee_id = Column(Integer, ForeignKey('employee.id'))
    maintenance_date = Column(DateTime, default=datetime.datetime.utcnow)
    details = Column(String, nullable=True)

class Billing(Base):
    """
    description: Table for billing and payment records for services.
    """
    __tablename__ = 'billing'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    appointment_id = Column(Integer, ForeignKey('appointment.id'))
    total_amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, nullable=True)
    status = Column(String, nullable=False, default='Pending')

class Repair(Base):
    """
    description: Table for engine repair services records.
    """
    __tablename__ = 'repair'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    boat_id = Column(Integer, ForeignKey('boat.id'))
    description = Column(String, nullable=True)
    repair_date = Column(DateTime, default=datetime.datetime.utcnow)
    cost = Column(Float, nullable=False)

class Cleaning(Base):
    """
    description: Table for cleaning service records.
    """
    __tablename__ = 'cleaning'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    boat_id = Column(Integer, ForeignKey('boat.id'))
    cleaning_date = Column(DateTime, default=datetime.datetime.utcnow)
    cost = Column(Float, nullable=False)

# Set up the engine and session
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
# Insert sample data into each table

# Adding customers
customer1 = Customer(name='John Doe', email='john.doe@example.com', phone='555-1234', address='123 Ocean Ave')
customer2 = Customer(name='Jane Smith', email='jane.smith@example.com', phone='555-5678', address='456 Harbor Ln')

# Adding boats
boat1 = Boat(name='Sea Explorer', type='Yacht', length=30.5, customer_id=1)
boat2 = Boat(name='Island Hopper', type='Sailboat', length=22.0, customer_id=2)

# Adding services
service1 = Service(name='Winterization', description='Boat winterization service', price=299.99)
service2 = Service(name='Engine Repair', description='Comprehensive engine repair', price=999.99)

# Adding appointments
appointment1 = Appointment(customer_id=1, boat_id=1, service_id=1, notes='First-time winterization')
appointment2 = Appointment(customer_id=2, boat_id=2, service_id=2, notes='Urgent engine repair')

# Adding parts
part1 = Part(name='Motor Oil', description='High performance motor oil', price=25.00)
part2 = Part(name='Boat Cover', description='Protective boat cover', price=180.00)

# Adding orders
order1 = Order(customer_id=1, part_id=1, quantity=4)
order2 = Order(customer_id=2, part_id=2, quantity=1)

# Adding employees
employee1 = Employee(name='George Wilson', position='Mechanic', hire_date=datetime.datetime(2022, 5, 15))
employee2 = Employee(name='Lisa Adams', position='Cleaner', hire_date=datetime.datetime(2023, 1, 10))

# Adding maintenance
maintenance1 = Maintenance(boat_id=1, employee_id=1, maintenance_date=datetime.datetime(2023, 9, 10), details='Annual engine check')
maintenance2 = Maintenance(boat_id=2, employee_id=2, maintenance_date=datetime.datetime(2023, 9, 11), details='Deck cleaning')

# Adding billing records
billing1 = Billing(appointment_id=1, total_amount=299.99, payment_date=datetime.datetime(2023, 10, 1), status='Paid')
billing2 = Billing(appointment_id=2, total_amount=999.99, payment_date=datetime.datetime(2023, 10, 2), status='Pending')

# Adding repairs
repair1 = Repair(boat_id=1, description='Engine overheating', repair_date=datetime.datetime(2023, 9, 5), cost=100.00)
repair2 = Repair(boat_id=2, description='Oil leak', repair_date=datetime.datetime(2023, 9, 7), cost=200.00)

# Adding cleaning records
cleaning1 = Cleaning(boat_id=1, cleaning_date=datetime.datetime(2023, 9, 12), cost=150.00)
cleaning2 = Cleaning(boat_id=2, cleaning_date=datetime.datetime(2023, 9, 13), cost=180.00)

# Add all records to session and commit
session.add_all([customer1, customer2, boat1, boat2, service1, service2,
                 appointment1, appointment2, part1, part2, order1, order2,
                 employee1, employee2, maintenance1, maintenance2, billing1,
                 billing2, repair1, repair2, cleaning1, cleaning2])

session.commit()
