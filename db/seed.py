from db import session
from faker import Faker
from models import Teacher, Group, Student, Subject, Grade

# Create a Faker instance
fake = Faker()

def create_groups():
    """
    Створення випадкових груп.
    """
    list_groups = ["1A", "1B", "1C"]
    groups = [Group(name=gr) for gr in list_groups]
    session.add_all(groups)

def create_teachers():
    """
    Створення випадкових вчителів.
    """
    teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
    session.add_all(teachers)

def create_students():
    """
    Створення випадкових студентів та призначення їх до груп.
    """
    students = [Student(fullname=fake.name(), group_id=fake.random_int(min=1, max=3)) for _ in range(30)]
    session.add_all(students)

def create_subjects():
    """
    Створення випадкових предметів (курсів) та призначення їх вчителям.
    """
    list_subjects = ["Math", "Literature", "IT", "Phisics", "Chemistry"]
    subjects = [Subject(name=subl, teacher_id=fake.random_int(min=1, max=5)) for subl in list_subjects]
    session.add_all(subjects)

def create_grades():
    """
    Створення випадкових оцінок для студентів у предметах (курсах).
    """
    students = session.query(Student).all()
    subjects = session.query(Subject).all()

    for student in students:
        for subject in subjects:
            grades = [Grade(grade=fake.random_int(min=2, max=5),
                            grade_date=fake.date_between(start_date='-1y', end_date='today'),
                            student_id=student.id, subject_id=subject.id) for _ in range(fake.random_int(min=3, max=5))]
            session.add_all(grades)

create_groups()
create_teachers()
create_students()
create_subjects()
create_grades()

session.commit()
session.close()