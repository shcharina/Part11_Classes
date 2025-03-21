class Student:
    def __init__(self, student_id, name, group) -> None:
        self.student_id = student_id
        self.name = name
        self.group = group
        self.grades = {}

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    def add_grade(self, subject, grade) -> None:
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def average_grade(self) -> float:
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    def subject_average_grade(self, subject) -> float:
        if not subject in self.grades:
            return 0
        all_grades_for_subject = self.grades.get(subject, [])
        if not all_grades_for_subject:
            return 0
        return sum(all_grades_for_subject) / len(self.grades.get(subject, []))

class Group:
    def __init__(self, group_id: str) -> None:
        self.group_id = group_id
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def average_grade(self) -> float:
        all_grades = [student.average_grade() for student in self.students]
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    def subject_average_grade(self, subject) -> float:
        all_grades = [student.subject_average_grade(subject) for student in self.students if subject in student.grades]
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

class Deanery:
    def __init__(self) -> None:
        self.groups = {}

    def add_group(self, group: Group) -> None:
        self.groups[group.group_id] = group

    def student_average_grade(self, student: Student) -> float:
        return student.average_grade()

    def student_subject_average(self, student: Student, subject: str) -> float:
        return student.subject_average_grade(subject)

    def group_average_grade(self, group: Group) -> float:
        return group.average_grade()

    def group_subject_average_grade(self, group: Group, subject: str) -> float:
        return group.subject_average_grade(subject)

    def students_for_dismissal(self, threshold: float = 2.5) -> list[Student]:
        students_for_dismissal = [student for group in self.groups.values() for student in group.students if
                student.average_grade() < threshold]
        return students_for_dismissal

    def scholarship_candidates(self, threshold : float = 4) -> list[Student]:
        return [student for group in self.groups.values() for student in group.students if
                student.average_grade() >= threshold]

