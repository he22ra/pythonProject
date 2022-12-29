'''
    1. 상속(inheritance)
        class 자식 클래스 이름 (부모 클래스 이름)
            pass

'''
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_human(self):
        print("=====인적사항=====")
        print(f"이름 : {self.name}  나이 : {self.age}")

class Teacher(Human):
    def __init__(self, name, age, teacher_id, subject, salary):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subject = subject
        self.salary = salary

    def show_teacher(self):
        print("====교직원 카드====")
        print(f"교직원 번호 : {self.teacher_id}")
        print(f"담당과목 : {self.subject}")
        print(f"급여 : {self.salary}")

teacher = Teacher("이순신", 40, 1, "컴퓨터", 300)
teacher.show_human()
teacher.show_teacher()

## student_id, grade, score
class Student(Human):
    def __init__(self, name, age, student_id, grade, score):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grade = grade
        self.score = score

    def show_student(self):
        print("====학생 카드====")
        print(f"학생 번호 : {self.student_id}")
        print(f"학년 : {self.grade}")
        print(f"성적 : {self.score}")


student = Student("학생A", 21, "201934-365147", "4학년", "B+")
student.show_human()
student.show_student()


