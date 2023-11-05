import random
from faker import Faker
from db.models import Teacher
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

fake = Faker()
engine = create_engine('postgresql://username:password@localhost/database')
Session = sessionmaker(bind=engine)
session = Session()

def seed_teachers(num_teachers):
    for _ in range(num_teachers):
        teacher = Teacher(name=fake.name())
        session.add(teacher)
    session.commit()

if __name__ == "__main__":
    num_teachers = 5
    seed_teachers(num_teachers)
