'''
Putthipong Phukhansung
633040224-3
Problem 5
'''

def add_emails():

    global email_info
    course_list = []
    email_info = {}


    while True:
        email = input("Enter an email address: ")
        if email == 'q' or email == 'Q':
            break

        course = input("Enter a course: ")
        if course == 'q' or course == 'Q':
            break
        course_list.append(course)

        email_info[email] = course
    return email_info


def print_email_info(arg):
    print(arg)


def print_course_info(arg):
    print("=== Writing emails and courses to file student.json ===")
    print("=== Reading emails and course from file students.json ===")
    print(end=" ")
    print(arg)

#
import json
def read_file():    
    with open('student.json') as file_json:
        data_read = json.load(file_json)
        for i in data_read["info"]:
            print(i["email"], end= "regiprintstered for course")
            print(i["course"])
#


if __name__ == "__main__":
    email_course = add_emails()
    print_email_info(email_course)
    print_course_info(email_course)