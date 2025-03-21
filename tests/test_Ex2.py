import pytest

from src.Ex2 import Student, Group, Deanery

def test_student():
    # Arrange & Act
    student = Student("001", "Иван Иванов", "4421")
    student.add_grade("УПД", 4)
    student.add_grade("УПД", 5)
    student.add_grade("Физкультура", 3)

    # Assert
    assert student.average_grade() == 4.0
    assert student.subject_average_grade("УПД") == 4.5
    assert student.subject_average_grade("Физкультура") == 3
    assert student.subject_average_grade("История") == 0

def test_group():
    # Arrange & Act
    group = Group("4421")
    student1 = Student("001", "Иван Иванов", "4421")
    student2 = Student("002", "Петр Петров", "4421")
    student1.add_grade("Математический анализ", 4)
    student2.add_grade("Математический анализ", 2)
    group.add_student(student1)
    group.add_student(student2)

    # Assert
    assert group.average_grade() == 3.0
    assert group.subject_average_grade("Математический анализ") == 3.0

def test_deanery():
    # Arrange & Act
    deanery = Deanery()
    group4421 = Group("4421")
    student1 = Student("001", "Иван Иванов", "4421")
    student2 = Student("002", "Петр Петров", "4421")
    student1.add_grade("Математический анализ", 2)
    student1.add_grade("Математический анализа", 2)
    student2.add_grade("Математический анализ", 5)
    student2.add_grade("УПД", 5)
    group4421.add_student(student1)
    group4421.add_student(student2)
    deanery.add_group(group4421)

    # Assert
    assert deanery.student_average_grade(student1) == 2
    assert deanery.group_subject_average_grade(group4421, "Математический анализ") == 3.5
    assert [student.name for student in deanery.students_for_dismissal()] == ["Иван Иванов"]
    assert [student.name for student in deanery.scholarship_candidates()] == ["Петр Петров"]