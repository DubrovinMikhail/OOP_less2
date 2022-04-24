class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        if len(self.grades) == 0:
            return 'Not grades'
        else:
            count = 0
            for grades_cours in self.grades:
                count += sum(self.grades[grades_cours])
            return round(count/len(self.grades), 2)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за домашние задания: {self.average_rating()} \n' \
              f'Курсы в процессе изучения: {" ,".join(self.courses_in_progress)} \n' \
              f'Завершенные курсы: {" ,".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.average_rating() > other.average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        if len(self.grades) == 0:
            return 'Not grades'
        else:
            count = 0
            for cours in self.grades:
                count += sum(self.grades[cours])
            return round(count/len(self.grades), 2)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за лекции: {self.average_rating()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecture):
            print('Not a Student')
            return
        return self.average_rating() > other.average_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname}'
        return res


stud_1 = Student('Marie', 'Curie', 'fam')
stud_1.finished_courses += ['OOP', 'Git', 'English']
stud_1.courses_in_progress += ['OOP', 'Git', 'English']

stud_2 = Student('Niels', 'Bohr', 'man')
stud_2.finished_courses += ['OOP', 'Git', 'English']
stud_2.courses_in_progress += ['OOP', 'Git', 'English']

lecture_1 = Lecture('David', 'Bohm')
lecture_1.courses_attached += ['English', 'Git']

lecture_2 = Lecture('Max', 'Planck')
lecture_2.courses_attached += ['Git', 'OOP']

reviewer_1 = Reviewer('Timothy', 'Berners-Lee')
reviewer_1.courses_attached += ['English', 'Git']
reviewer_1.rate_hw(stud_1, 'English', 8)
reviewer_1.rate_hw(stud_1, 'Git', 6)
reviewer_1.rate_hw(stud_2, 'English', 9)

reviewer_2 = Reviewer('Alexander', 'Fleming')
reviewer_2.courses_attached += ['OOP']

stud_1.rate_hw(lecture_1, 'Git', 9)
stud_2.rate_hw(lecture_1, 'Git', 6)
stud_2.rate_hw(lecture_1, 'English', 7)
stud_1.rate_hw(lecture_2, 'OOP', 2)
stud_2.rate_hw(lecture_2, 'OOP', 4)

print(lecture_1)
print(lecture_2)

print(stud_1 > stud_2)
print(lecture_1 > lecture_2)

student_list = [stud_1, stud_2]
lecture_list = [lecture_1, lecture_2]


def average_rating_all_student(stud_list, student_cours):
    counter = 0
    counter_grades = 0
    for student in stud_list:
        if student_cours in student.grades:
            counter_grades += sum(student.grades[cours])
            counter += len(student.grades[cours])
    return round(counter_grades/counter, 2)


def average_rating_all_lecture(stud_list, cours):
    counter = 0
    counter_grades = 0
    for lecture in lecture_list:
        if cours in lecture.grades:
            counter_grades += sum(lecture.grades[cours])
            counter += len(lecture.grades[cours])
    return round(counter_grades/counter, 2)


