'''
Putthipong Phukhansung
633040224-3
'''

class Teacher:
    def __init__(self, name, address, subject, *course_ids):
        self.name = name
        self.course_ids = course_ids
        self.address = address
        self.subject = subject

    def print_office_no(self):
        return(f"{self.name} has the office at {self.address}")

    def print_research_work(self):
        return(f"{self.name} is doing research in these topics {self.subject}")

    def print_courses_work(self):
        return(f"{manee.name} teacher these course {manee.subject}")


if __name__ == '__main__':
    manee = Teacher("Manee", "Rm. 4203", "Artificial Intelligence", "EN842004", "EN813703")
    mana = Teacher("Mana", "Rm. 4209", "Internet of Things", "EN84005", "EN813703")
    manee.print_office_no()
    manee.print_research_work()
    manee.print_courses_work()
    mana.print_office_no()
    mana.print_research_work()
    mana.print_courses_work