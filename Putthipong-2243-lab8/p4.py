'''
Putthipong Phukhansung
633040224-3
Problem 4
'''


class ComEnStudent:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def __str__(self):
        return (f"{self.name} has taken these courses: {self.course}")

    def take_courses(self, *course):
        for i in course:
            self.course.append(i)

class CoEStudent(ComEnStudent):
    def __init__(self, name, *course):
        super().__init__(name, *course)

class DMEStudent(ComEnStudent):
    head: object

    def __init__(self, name, *course):
        super().__init__(name, *course)

    def make_content_type(self, head):
        self.head = head
        return (f"specialized in creating content type:{head}")

    def __str__(self):
        return (f"{self.name} has taken these courses: {self.course}\n {self.make_content_type(self.head)}")


if __name__ == "__main__":
    com_students = []
    manee = CoEStudent("Manee", ["EN813701"])
    mana = DMEStudent("Mana", ["EN842004"])
    manee.take_courses("EN813702", "EN811301", "EN811302")
    mana.take_courses("EN842005")
    mana.make_content_type("Infographics")
    com_students.append(manee)
    com_students.append(mana)
    for com_student in com_students:
        com_student.take_courses("SC401206")
        print(com_student)