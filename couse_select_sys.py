class Courses:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period


class Students:
    func_list = [
        {"func": "Select a course", "name": "select_course"},
        {"func": "View course selected", "name": "show_selected_course"},
        {"func": "Delete a selected course", "name": "show_deleted_course"},
    ]

    def __init__(self, name):
        self.name = name
        self.courses = []

    def select_course(self, courses_list):
        """
        select distinct courses
        :return:
        """
        while True:
            for i, item in enumerate(courses_list, 1):
                print(i, item.name, item.price, item.period)
            user_choice = input("Which course number do you want to select? Or type 'q' for exit")
            if user_choice != "q":
                course_num = int(user_choice) - 1
                if courses_list[course_num] not in self.courses:
                    self.courses.append(courses_list[course_num])
            elif user_choice == "q":
                break

    def show_selected_course(self, courses_list):
        """
        show courses selected
        :return:
        """
        print("You've selected the following course:")
        for item in self.courses:
            print(f"{item.name}  {item.price}  {item.period}")

    def show_deleted_course(self, courses_list):
        """
        delete course selected
        :return:
        """
        while True:
            for i, item in enumerate(self.courses, 1):
                print(i, item.name)
            user_choice = input("Which course do you want to delete? Please select a number or type 'q' for exit")
            if user_choice == "q":
                break
            else:
                course_num = int(user_choice) - 1
                del self.courses[course_num]


def run():
    course_list = []
    for num in range(10):
        course = Courses(f"coding{num + 1}", 90 + num, 90)
        course_list.append(course)

    student_name = input("What is your name?")

    student = Students(student_name)

    while True:
        for i, item in enumerate(Students.func_list, 1):
            print(i, item["func"])
        choice = int(input("Please select an option."))
        num = choice - 1
        row = Students.func_list[num]
        name = row["name"]
        func = getattr(student, name)
        func(course_list)


if __name__ == "__main__":
    run()
