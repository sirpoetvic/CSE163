# Student Class, CP4, Lesson 13
# need to redo this, logic is wrong.
# specifically on the init.
class Student():
    def __init__(self, student_number, file_name):
        """
        Args:
            student_number (int): ID #
            classes (dict): classes as key, credit # as value
        """
        self.student_number = student_number
        self.name = file_name[:-4]  # removes last 4 letters of the file name
        self.classes = {}
        with open(file_name, 'r') as file:
            f = file.readlines()
            for line in f:
                key, value = line.strip().split()
                self.classes[key] = value

    def get_name(self):
        return self.name

    def get_student_number(self):
        return self.student_number

    def get_credits_for(self, class_name):
        # use the class code
        credit_list = []
        for key, value in self.classes.items():
            if class_name in key:
                credit_list.append(value)
        if len(credit_list) == 0:
            return 0
        else:
            # assumes only one class is passed only
            return credit_list[0]

    def get_classes(self):
        class_list = []
        for key in self.classes:
            class_list.append(self.classes[key])
        return class_list
