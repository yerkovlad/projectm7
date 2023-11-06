from sqlalchemy import func, desc
from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session


def select_01():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    """
    result = session.query(
        Student.id,
        Student.fullname,
        func.round(func.avg(Grade.grade), 2).label('average_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return result


def select_02():
    """
    Знайти студента із найвищим середнім балом з певного предмета.
    """
    result = session.query(
        Student.id,
        Student.fullname,
        func.round(func.avg(Grade.grade), 2).label('average_grade')
    ).join(Grade).filter(Grade.subject_id == 1).group_by(Student.id).order_by(desc('average_grade')).limit(1).all()
    return result


def select_03():
    """
    Знайти середній бал у групах з певного предмета.
    """
    result = session.query(
        Group.name.label('group_name'),
        func.round(func.avg(Grade.grade), 2).label('average_grade')
    ).join(Student, Group.id == Student.group_id).join(Grade, Student.id == Grade.student_id).join(Subject, Grade.subject_id == Subject.id).filter(Subject.name == "IT").group_by(Group.name).order_by(desc('average_grade')).all()
    return result


def select_04():
    """
    Знайти середній бал на потоці (по всій таблиці оцінок).
    """
    result = session.query(func.round(func.avg(Grade.grade), 2).label('overall_average_grade')).scalar()
    return result


def select_05():
    """
    Знайти які курси читає певний викладач.
    """
    result = session.query(Subject.name.label('subject_name')).join(Teacher).filter(Teacher.fullname == "Matthew Rush").all()
    return result


def select_06():
    """
    Знайти список студентів у певній групі.
    """
    result = session.query(Student.fullname.label('student_name')).join(Group).filter(Group.name == "1A").all()
    return result


def select_07():
    """
    Знайти оцінки студентів у окремій групі з певного предмета.
    """
    result = session.query(Student.fullname.label('student_name'), Grade.grade.label('grade')).join(Group).join(Grade).join(Subject).filter(Group.name == "1A", Subject.name == "IT").all()
    return result


def select_08():
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    """
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade_by_teacher')).join(Subject).join(Teacher).filter(Teacher.fullname == "Matthew Rush").scalar()
    return result


def select_09():
    """
    Знайти список курсів, які відвідує певний студент.
    """
    result = session.query(Subject.name.label('subject_name')).join(Grade).join(Student).filter(Student.fullname == 'Bryan Campbell').group_by(Subject.name).all()
    return result


def select_10():
    """
    Список курсів, які певному студенту читає певний викладач.
    """
    result = session.query(Subject.name.label('subject_name')).join(Teacher).join(Grade).join(Student).filter(Student.fullname == 'Bryan Campbell', Teacher.fullname == "Matthew Rush").group_by(Subject.name).all()
    return result


if __name__ == '__main__':
    print(select_01())
    print(select_02())
    print(select_03())
    print(select_04())
    print(select_05())
    print(select_06())
    print(select_07())
    print(select_08())
    print(select_09())
    print(select_10())