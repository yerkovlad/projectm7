from db.models import Student, Grade
from sqlalchemy import func, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('postgresql://username:password@localhost/database')
Session = sessionmaker(bind=engine)
session = Session()

def select_students_with_highest_avg_score(num_students=5):
    subquery = session.query(Grade.student_id, func.avg(Grade.score).label('avg_score'))
    subquery = subquery.group_by(Grade.student_id).subquery()

    query = session.query(Student, subquery.c.avg_score)
    query = query.join(subquery, Student.id == subquery.c.student_id)
    query = query.order_by(desc(subquery.c.avg_score)).limit(num_students)
    
    return query.all()

results = select_students_with_highest_avg_score()
for student, avg_score in results:
    print(f"Student: {student.fullname}, Average Score: {avg_score}")