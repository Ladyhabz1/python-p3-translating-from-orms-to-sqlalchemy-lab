from models import Dog, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Set up the database engine and session
engine = create_engine('sqlite:///dogs.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_table(base, engine):
    """Create all tables in the database."""
    base.metadata.create_all(engine)

def save(session, dog):
    """Save a Dog instance to the database."""
    session.add(dog)
    session.commit()

def get_all(session):
    """Return all dogs."""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Find a dog by its name."""
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    """Find a dog by its ID."""
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    """Find a dog by both name and breed."""
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, new_breed):
    """Update a dog's breed."""
    dog.breed = new_breed
    session.commit()
