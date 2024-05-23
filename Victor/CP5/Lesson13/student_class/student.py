# Student Class, CP4, Lesson 13
class Student:
    def __init__(self, student_number, file_name):
        self.student_number = student_number
        self.name = file_name
        self.classes = {}
        with open(file_name) as file:
            f = file.readlines()
            for line in f:
                key, value = line.strip().split()
                self.classes[key] = value

    def get_name(self):
        relative_path = self.name.split("\\")[-1]
        self.name = relative_path[:-4]
        return self.name

    def get_student_number(self):
        return self.student_number

    def get_credits_for(self, class_name):
        credit_list = []
        for key, value in self.classes.items():
            if class_name in key:
                credit_list.append(value)
        if len(credit_list) == 0:
            return 0
        else:
            return credit_list[0]

    def get_classes(self):
        class_list = []
        for key in self.classes:
            class_list.append(self.classes[key])
        return class_list
