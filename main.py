#Задание 1
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

#Задание 2

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_Lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'MAN')
best_student.courses_in_progress += ['Python']

cool_lec = Lecturer('Some', 'Buddy')
cool_lec.courses_attached += ['Python']

best_student.rate_Lecturer(cool_lec, 'Python', 10)
best_student.rate_Lecturer(cool_lec, 'Python', 10)

print(cool_lec.grades)


#Задание 3

class Reviewer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Имя: {self.first_name}\nФамилия: {self.last_name}"

class Lecturer:
    def __init__(self, first_name, last_name, rating):
        self.first_name = first_name
        self.last_name = last_name
        self.rating = rating

    def __str__(self):
        return (f"Имя: {self.first_name}\n"
                f"Фамилия: {self.last_name}\n"
                f"Средняя оценка за лекции: {self.rating:.1f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.rating < other.rating
        return NotImplemented

class Student:
    def __init__(self, first_name, last_name, homework_grade, courses_in_progress, completed_courses):
        self.first_name = first_name
        self.last_name = last_name
        self.homework_grade = homework_grade
        self.courses_in_progress = courses_in_progress
        self.completed_courses = completed_courses

    def __str__(self):
        return (f"Имя: {self.first_name}\n"
                f"Фамилия: {self.last_name}\n"
                f"Средняя оценка за домашние задания: {self.homework_grade:.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.completed_courses)}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.homework_grade < other.homework_grade
        return NotImplemented

# Пример использования исправленного кода
reviewer = Reviewer("Какой-то", "Приятель")
lecturer = Lecturer("Some", "Buddy", 9.9)
student = Student("Ruoy", "Eman", 9.9, ["Python", "Git"], ["Введение в программирование"])

print(reviewer)
print(lecturer)
print(student)

# Сравнение лекторов
lecturer1 = Lecturer("Лектор1", "Фамилия1", 8.5)
lecturer2 = Lecturer("Лектор2", "Фамилия2", 9.0)
print(lecturer1 < lecturer2)

# Сравнение студентов
student1 = Student("Студент1", "Фамилия1", 8.0, ["Python"], ["Введение в программирование"])
student2 = Student("Студент2", "Фамилия2", 9.5, ["Git"], ["Введение в программирование"])
print(student1 < student2)


#Задание 4

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, course, grade):
        if course not in self.grades:
            self.grades[course] = []
        self.grades[course].append(grade)

    def get_grades(self, course):
        return self.grades.get(course, [])

class Lecturer:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, course, grade):
        if course not in self.grades:
            self.grades[course] = []
        self.grades[course].append(grade)

    def get_grades(self, course):
        return self.grades.get(course, [])

def average_student_grade(students, course):
    total_grades = 0
    count = 0
    for student in students:
        grades = student.get_grades(course)
        total_grades += sum(grades)
        count += len(grades)
    return total_grades / count if count > 0 else 0

def average_lecturer_grade(lecturers, course):
    total_grades = 0
    count = 0
    for lecturer in lecturers:
        grades = lecturer.get_grades(course)
        total_grades += sum(grades)
        count += len(grades)
    return total_grades / count if count > 0 else 0

# Пример использования
student1 = Student("Alice")
student1.add_grade("Math", 90)
student1.add_grade("Math", 80)

student2 = Student("Bob")
student2.add_grade("Math", 70)
student2.add_grade("Math", 60)

lecturer1 = Lecturer("Dr. Smith")
lecturer1.add_grade("Math", 85)
lecturer1.add_grade("Math", 95)

lecturer2 = Lecturer("Dr. Johnson")
lecturer2.add_grade("Math", 75)
lecturer2.add_grade("Math", 80)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print("Average student grade in Math:", average_student_grade(students, "Math"))
print("Average lecturer grade in Math:", average_lecturer_grade(lecturers, "Math"))